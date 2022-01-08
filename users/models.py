from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

class Biodata(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    telp = models.CharField(max_length=16, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nama)
    
    class Meta:
        verbose_name_plural ="Biodata"

class API(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username