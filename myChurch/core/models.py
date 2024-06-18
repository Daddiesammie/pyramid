from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phoneNumber=models.CharField(max_length=12)
    description=models.TextField()

    def __str__(self) : 
        return f'Message from {self.name}'


class Payment(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='payment_photos/', blank=True, null=True)

    def __str__(self):
        return f'Message from {self.name}'
    
class AccDet(models.Model):
    name = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=100, null=True)
    bank = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to='account_photos', null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name