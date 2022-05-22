from django.db import models
from datetime import datetime
# Create your models here.
class machine (models.Model):
    name = models.CharField(max_length=100)
    describtion = models.TextField()
    publishdate = models.DateField(default=datetime.now)
    photo = models.ImageField(upload_to='photos')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-publishdate']
