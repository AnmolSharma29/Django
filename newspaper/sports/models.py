from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField

class Sports(models.Model):
    sports_heading=models.CharField(max_length=300)
    sports_category=models.CharField(max_length=50)
    sports_date=models.DateTimeField(default=timezone.now)
    sports_image=models.ImageField(upload_to='images/')
    sports_des=models.TextField()

    sports_slug = AutoSlugField(populate_from='sports_heading',unique=True,null=True,default=None)

    def __str__(self):
        return self.sports_heading
# Create your models here.
