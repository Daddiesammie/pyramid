from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='account_photos')
    description = models.TextField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.name