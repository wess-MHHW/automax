from django.contrib import admin

from main.models import Listing

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    readonly_fields= ('id','vin',)

admin.site.register(Listing, ListingAdmin)