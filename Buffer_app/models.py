from django.db import models

class Publication(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='publication_images/')
    header = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    
