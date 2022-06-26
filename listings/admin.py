from django.contrib import admin

# Register your models here.
from listings.models import Listing
from .forms import ListingsForm


class ListingAdmin(admin.ModelAdmin):
    form = ListingsForm


admin.site.register(Listing, ListingAdmin)
