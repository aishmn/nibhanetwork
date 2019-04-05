from django.contrib import admin
from .models import Post, Message, Notification
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_per_page = 30
admin.site.register(Post, PostAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_per_page = 30
admin.site.register(Message, MessageAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_per_page = 30
admin.site.register(Notification, NotificationAdmin)