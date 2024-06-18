from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='project_photos')
    description = models.TextField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.name