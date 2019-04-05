from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Epin(models.Model):
    serial_no = models.CharField(max_length=200,unique=True)
    pin_value = models.IntegerField()
    pin_name = models.CharField(max_length=50, blank=True, null=True)
    used = models.BooleanField(default=False, blank=True, null=True)
    used_by = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    used_at = models.DateTimeField(blank=True, null=True,auto_now=False, auto_now_add=False)
    sold_to = models.CharField(max_length=250, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.serial_no
