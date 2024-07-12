from django.contrib import admin
from sports.models import Sports
class SportsAdmin(admin.ModelAdmin):
    list_display=('sports_heading','sports_category','sports_date','sports_image','sports_des')

admin.site.register(Sports,SportsAdmin)
# Register your models here.
