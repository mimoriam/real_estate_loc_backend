from django.db import models

from django.utils import timezone
from django.contrib.gis.geos import Point
from django.contrib.gis.db import models

from django.contrib.auth import get_user_model

import PIL
from io import BytesIO
from django.core.files import File

User = get_user_model()


def compress(picture):
    if picture:
        pic = PIL.Image.open(picture)
        buf = BytesIO()
        pic.save(buf, 'JPEG', quality=50)
        new_pic = File(buf, name=picture.name)
        return new_pic
    else:
        return None


class Listing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    choices_area = (
        ('Inner London', 'Inner London'),
        ('Outer London', 'Outer London'),
    )
    area = models.CharField(max_length=30, blank=True, null=True, choices=choices_area)

    borrow = models.CharField(max_length=50, blank=True, null=True)

    choices_listing_type = (
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Office', 'Office'),
    )
    listing_type = models.CharField(max_length=20, choices=choices_listing_type)

    choices_property_status = (
        ('Sale', 'Sale'),
        ('Rent', 'Rent'),
    )
    property_status = models.CharField(max_length=20, blank=True, null=True, choices=choices_property_status)

    price = models.DecimalField(max_digits=50, decimal_places=0)

    choices_rental_frequency = (
        ('Month', 'Month'),
        ('Week', 'Week'),
        ('Day', 'Day'),
    )
    rental_frequency = models.CharField(max_length=20, blank=True, null=True, choices=choices_rental_frequency)

    rooms = models.IntegerField(blank=True, null=True)
    furnished = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    # location = models.PointField(blank=True, null=True, srid=4326)
    # Location field no longer needed as we need to reverse geocode now

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    picture = models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        new_pic = compress(self.picture)
        self.picture = new_pic  # Do these two lines for multiple images if exist in more fields

        super().save(*args, **kwargs)


class PointsOfInterest(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)

    choices_type = (
        ('University', 'University'),
        ('Hospital', 'Hospital'),
        ('Stadium', 'Stadium')
    )
    type = models.CharField(max_length=50, choices=choices_type)
    location = models.PointField(srid=4326, blank=True, null=True)

    def __str__(self):
        return self.name
