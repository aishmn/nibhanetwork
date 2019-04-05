from django.contrib import admin
from .models import Franchise
# Register your models here.

class FranchiseAdmin(admin.ModelAdmin):
    list_display = ('franchise_name','franchise_contact_no','aadhar_card_no',)
    list_display_links= ('franchise_name',)
    list_filter = ('franchise_bank_name',)
    search_fields = ('franchise_name','franchise_contact_no',)
    list_per_page = 30
admin.site.register(Franchise, FranchiseAdmin)  