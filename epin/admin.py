from django.contrib import admin
from .models import Epin
# Register your models here.

class EpinAdmin(admin.ModelAdmin):
    list_display = ('id','serial_no','used_by','used','used_at','pin_name','pin_value')
    list_display_links= ('serial_no',)
    list_filter = ('used','pin_value')
    search_fields = ('serial_no','used_by__username')
    list_per_page = 30
admin.site.register(Epin, EpinAdmin)