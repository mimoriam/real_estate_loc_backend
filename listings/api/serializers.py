from rest_framework import serializers
from listings.models import Listing, PointsOfInterest
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point


class ListingSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    seller_user = serializers.SerializerMethodField()
    seller_agency_name = serializers.SerializerMethodField()
    listing_points_of_interest = serializers.SerializerMethodField()

    def get_seller_agency_name(self, obj):
        return obj.seller.profile.agency_name

    def get_seller_user(self, obj):
        return obj.seller.username

    def get_country(self, obj):
        return "England"

    def get_listing_points_of_interest(self, obj):
        listing_loc = Point(obj.latitude, obj.longitude, srid=4326)
        query = PointsOfInterest.objects.filter(location__distance_lte=(listing_loc, D(km=10)))
        query_serialized = PointsOfInterestSerializer(query, many=True)
        return query_serialized.data

    class Meta:
        model = Listing
        fields = '__all__'


class PointsOfInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointsOfInterest
        fields = '__all__'
