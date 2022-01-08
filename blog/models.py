from django.contrib.auth.models import User
from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Kategori"
    

class Artikel(models.Model):
    nama = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    judul = models.CharField(max_length=100)
    body = RichTextUploadingField(blank=True, null=True,
                                config_name='special',
                                external_plugin_resources=[(
                                    'youtube',
                                    '/static/ckeditor_plugins/youtube/youtube/',
                                    'plugin.js',
                                )]
)
    kategory = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='artikel/thumbnail', blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)

    def ImgUrl(self):
        if self.thumbnail == '' or self.thumbnail == None:
            gambar = 'http://localhost:8000/static/default_thumbnail.jpg'
        else:
            gambar = self.thumbnail.url
        return gambar

    class Meta:
        ordering =['-date']
        verbose_name_plural = "Artikel"