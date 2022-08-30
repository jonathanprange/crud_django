from django.db import models
from uuid import uuid4
from .enums import RegionType

# Create your models here.
class Regions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    name =  models.CharField(max_length=255)
    region_type = models.CharField(max_length=12, choices=RegionType.choices(), default=RegionType.CITY)
    postal_code_range_start = models.CharField(max_length=8)
    postal_code_range_end = models.CharField(max_length=8)
    created_at = models.DateField(auto_now_add=True)
