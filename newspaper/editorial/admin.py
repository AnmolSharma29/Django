from django.contrib import admin
from editorial.models import Editorial
class EditorialAdmin(admin.ModelAdmin):
    list_display=('editorial_heading','editorial_category','editorial_date','editorial_image','editorial_des')

admin.site.register(Editorial,EditorialAdmin)
# Register your models here.
