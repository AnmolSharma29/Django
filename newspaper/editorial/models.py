from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
class Editorial(models.Model):
    editorial_heading=models.CharField(max_length=300)
    editorial_category=models.CharField(max_length=50)
    editorial_date=models.DateTimeField(default=timezone.now)
    editorial_image=models.ImageField(upload_to='images/')
    editorial_des=models.TextField()

    editorial_slug = AutoSlugField(populate_from='editorial_heading',unique=True,null=True,default=None)

    def __str__(self):
        return self.editorial_heading
    
# Create your models here.
