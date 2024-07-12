from django.db import models
from django.utils import timezone
import datetime

class topNews(models.Model):
    topNews_heading=models.CharField(max_length=300)
    topNews_category=models.CharField(max_length=50)
    topNews_date=models.DateTimeField(default=timezone.now)
    topNews_image=models.ImageField(upload_to='images/')
    topNews_des=models.TextField()

    def __str__(self):
        return self.topNews_heading