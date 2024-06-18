from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='gallery_photos')
    def __str__(self):
        return self.name