from django.db import models

# Create your models here.
class mineral(models.Model):
	name = models.CharField(max_length=200)
	price = models.IntegerField(default=0)
