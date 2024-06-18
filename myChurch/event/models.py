from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='event_photos')
    description = models.TextField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.name