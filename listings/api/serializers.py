from rest_framework import serializers
from listings.models import Listing


class ListingSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    seller_user = serializers.SerializerMethodField()

    def get_seller_user(self, obj):
        return obj.seller.username

    def get_country(self, obj):
        return "England"

    class Meta:
        model = Listing
        fields = '__all__'
