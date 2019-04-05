from django.contrib import admin
from .models import SingleLegIncome, RoyaltyIncome, WithdrawlBill, Closing, DirectSponsorIncome, GrandTotal
from .models import Profile
from import_export.admin import ImportExportModelAdmin

from import_export import resources

class SingleLegResource(resources.ModelResource):
    class Meta:
        model = SingleLegIncome
        exclude = ()
        fields = ()
        export_order = ()

class DirectSponsorResource(resources.ModelResource):
    class Meta:
        model = DirectSponsorIncome

class RoyaltyResource(resources.ModelResource):
    class Meta:
        model = RoyaltyIncome

class WithdrawlResource(resources.ModelResource):
    class Meta:
        model = WithdrawlBill

class ClosingResource(resources.ModelResource):
    class Meta:
        model = Closing

class GrandTotalResource(resources.ModelResource):
    class Meta:
        model = GrandTotal


@admin.register(SingleLegIncome)
class SingleLegExport(ImportExportModelAdmin):
	resource_class = SingleLegResource
	list_display = ('profile', 'level','ammount', 'remaining',)
	list_display_links= ('profile',)
	list_filter = ('level',)
	search_fields = ('profile__user__username', 'level',)
	list_per_page = 30

@admin.register(DirectSponsorIncome)
class DirectSponsorExport(ImportExportModelAdmin):
	resource_class = DirectSponsorResource
	list_display = ('profile', 'level','ammount', 'remaining',)
	list_display_links = ('profile',)
	list_filter = ('level',)
	search_fields = ('profile__user__username', 'level',)
	list_per_page = 30

@admin.register(RoyaltyIncome)
class RoyaltyExport(ImportExportModelAdmin):
	resource_class = RoyaltyResource
	list_display = ('id','profile', )
	list_display = ('profile', 'level','ammount', 'remaining',)
	list_display_links = ('profile',)
	list_filter = ('level',)
	search_fields = ('profile__user__username', 'level',)
	list_per_page = 30

@admin.register(WithdrawlBill)
class WithdrawlExport(ImportExportModelAdmin):
	resource_class = WithdrawlResource
	list_display = ('profile','date','ammount', 'paid', 'method')
	list_display_links = ('profile',)
	date_hierarchy = 'date'
	list_filter = ('date',)
	search_fields = ('profile__user__username', 'date',)
	list_per_page = 30

@admin.register(Closing)
class ClosingExport(ImportExportModelAdmin):
	resource_class = ClosingResource
	list_display = ('date','ammount', 'total_user',)
	date_hierarchy = 'date'
	list_display_links = ('date',)
	list_filter = ('date',)
	search_fields = ('profile__user__username', 'date',)
	list_per_page = 30

@admin.register(GrandTotal)
class GrandTotalExport(ImportExportModelAdmin):
	resource_class = GrandTotalResource
	list_display = ('profile','total', 'withdrawn', 'remaining',)
	list_display_links = ('profile',)
	list_filter = ()
	search_fields = ('profile__user__username',)
	list_per_page = 30
