from django.db import models
from accounts.models import Profile
# Create your models here.


class Post(models.Model):
    profile = models.ForeignKey(Profile, related_name='post_profile', on_delete=models.CASCADE)
    blog = models.TextField(blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post-image', height_field=None, blank=True, width_field=None, max_length=None)
    def __str__(self):
        return self.title

class Message(models.Model):
    send_by = models.ForeignKey(Profile, related_name='message_sendby', on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    send_to = models.ForeignKey(Profile, related_name='message_sendto',blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.send_by)

class Notification(models.Model):
    notice = models.TextField(blank=True, null=True)
    author = models.CharField(blank=True, null=True, max_length=50)
    date = models.DateTimeField(auto_now_add=False)
    def __str__(self):
        return self.notice