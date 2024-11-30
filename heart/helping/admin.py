from django.contrib import admin
from .models import Donor,Volunteer,DonationArea,Donation,Gallery

# Register your models here.

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_dispaly = ('id','user','contact','address','regdate')

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_diaplay = ('id','user','contact','address','regdate')

@admin.register(DonationArea)
class DonationAreaAdmin(admin.ModelAdmin):
    list_display =('id','areaname','description','creationdodate')

@admin.register(Donation)
class DonataeAdmin(admin.ModelAdmin):
    list_display = ('id','donor','volunteer','donationarea','donationname')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id','donation','deliverypic','creationdate')

# Register your models here.
