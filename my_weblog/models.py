from django.db import models


class post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

# Create your models here.
