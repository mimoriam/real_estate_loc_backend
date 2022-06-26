from django.contrib import admin
from listings.models import Listing, PointsOfInterest

from .forms import PointsOfInterestForm


class PointsOfInterestAdmin(admin.ModelAdmin):
    form = PointsOfInterestForm


# admin.site.register(Listing, ListingAdmin)
admin.site.register(Listing)
admin.site.register(PointsOfInterest, PointsOfInterestAdmin)
