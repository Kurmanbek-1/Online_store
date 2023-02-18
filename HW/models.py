from django.db import models

# Create your models here.

class Hashtag(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title

class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField(default=0.0)
    hashtags = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title


