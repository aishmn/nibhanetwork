from django.db import models

# Create your models here.
class Terms(models.Model):
    title = models.CharField(max_length=50)
    term = models.TextField()

    class Meta:
        ordering = ('title', )
        verbose_name = 'Term'
        verbose_name_plural = 'Terms'
    
    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.ImageField(upload_to='Gallery/%Y/%m/%d', blank=True)
    image_title = models.CharField(max_length=100)
    image_uploaded_by = models.CharField(max_length=50)
    description = models.CharField(max_length = 250, blank=True, null=True)
    def __str__(self):
        return self.image_title 