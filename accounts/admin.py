from django.contrib import admin
from .models import Profile
from payments.models import WithdrawlBill, SingleLegIncome, RoyaltyIncome, DirectSponsorIncome
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin
from django.utils import timezone
from import_export import resources

class ProfileResource(resources.ModelResource):
    class Meta:
    	model = Profile
    	exclude = ()
    	fields = ('id','user__username', 'full_name','user_contact_no', 'user_bank_name','user_bank_ac_no','user_bank_IFSC','activated','paytm','phonepay','googlepay','aadhar_card_no','pan_card_no')
    	export_order = ()

def activate(modeladmin, request, queryset):
 	queryset.update(
 		activated = True,
 		activated_date = timezone.now()
 		)
activate.short_description = 'Activate these Profiles'

class WithdrawlInline(admin.TabularInline):
	model = WithdrawlBill
	min = 0
	raw_id_fields = ('profile',)

class SingleLegIncomeInline(admin.TabularInline):
	model = SingleLegIncome
	min_num = 0
	max_num = 20
	extra = 1
	raw_id_fields = ()
class RoyaltyIncomeInline(admin.TabularInline):
	model = RoyaltyIncome
	min_num = 0
	max_num = 20
	extra = 1
	raw_id_fields = ()

class DirectSponsorIncomeInline(admin.TabularInline):
	model = DirectSponsorIncome
	min_num = 0
	max_num = 20
	extra = 1
	raw_id_fields = ()
	filter_horizontal = ['users',]


@admin.register(Profile)
class ProfileExport(ImportExportModelAdmin):
	resource_class = ProfileResource
	actions = [activate]
	inlines = [WithdrawlInline, SingleLegIncomeInline, RoyaltyIncomeInline, DirectSponsorIncomeInline]
	date_hierarchy = 'activated_date'
	list_display = ('user','full_name', 'user_contact_no', 'user_bank_IFSC', 'user_bank_name','user_bank_ac_no','paytm','phonepay','googlepay','activated',)
	list_display_links = ('user',)
	filter_horizontal = ['sponsored_user',]
	list_filter = ('activated','activated_date')
	search_fields = ('user__username', 'full_name', 'user_contact_no',)
	list_per_page = 30