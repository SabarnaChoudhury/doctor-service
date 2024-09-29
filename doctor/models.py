from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.IntegerField()
    email = models.EmailField(max_length=100, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    image = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name
