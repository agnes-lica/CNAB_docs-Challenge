from django.db import models

class Store(models.Model):
    
    name = models.CharField(max_length=14, unique=True)
    owner = models.CharField(max_length=19)
