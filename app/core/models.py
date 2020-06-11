from django.db import models

class Recipe(models.Model):
    """Recipe model"""
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
