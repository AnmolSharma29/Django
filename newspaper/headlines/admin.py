from django.contrib import admin
from headlines.models import Headlines
class HeadlineAdmin(admin.ModelAdmin):
    list_display=('headline'),

admin.site.register(Headlines,HeadlineAdmin)
# Register your models here.
