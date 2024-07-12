from django.db import models
from django.utils import timezone
class Sports(models.Model):
    sports_heading=models.CharField(max_length=300)
    sports_category=models.CharField(max_length=50)
    sports_date=models.DateTimeField(default=timezone.now)
    sports_image=models.ImageField(upload_to='images/')
    sports_des=models.TextField()

    def __str__(self):
        return self.sports_heading
# Create your models here.
