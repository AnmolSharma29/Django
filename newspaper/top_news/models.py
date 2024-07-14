from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField

class topNews(models.Model):
    topNews_heading=models.CharField(max_length=300)
    topNews_category=models.CharField(max_length=50)
    topNews_date=models.DateTimeField(default=timezone.now)
    topNews_image=models.ImageField(upload_to='images/')
    topNews_des=models.TextField()

    slug = AutoSlugField(populate_from='topNews_heading',unique=True,null=True,default=None)

    def __str__(self):
        return self.topNews_heading