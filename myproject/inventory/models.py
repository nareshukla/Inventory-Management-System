from django.db import models

# Create your models here.
from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
