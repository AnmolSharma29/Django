from django.contrib import admin
from top_news.models import topNews
class topNewsAdmin(admin.ModelAdmin):
    list_display = ('topNews_heading', 'topNews_category', 'topNews_date','topNews_image','topNews_des')

admin.site.register(topNews,topNewsAdmin)
# Register your models here.
