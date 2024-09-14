from django.contrib import admin

from main.models import LikedListing, Listing

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    readonly_fields= ('id','vin',)

class LikedListingAdmin(admin.ModelAdmin):
    readonly_fields= ('id', )

admin.site.register(Listing, ListingAdmin)
admin.site.register(LikedListing, LikedListingAdmin)