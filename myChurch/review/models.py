from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='review_photos')
    description = models.TextField()

    def __str__(self):
        return self.name