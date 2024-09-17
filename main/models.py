import uuid
from django.db import models

class Potion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    caution = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    def __str__(self):
        return self.name
