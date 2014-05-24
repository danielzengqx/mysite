from django.db import models

# Create your models here.
class FlowDrawer(models.Model):
	flow = models.CharField(max_length=200)
