from django.db import models
from accounts.models import Profile
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Closing(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    ammount = models.BigIntegerField(null=True, blank=True)
    total_user = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.date.strftime('%m/%d/%Y')

class SingleLegIncome(models.Model):
    level_one = 'level_one'
    level_two = 'level_two'
    level_three = 'level_three'
    level_four = 'level_four'
    level_five = 'level_five'
    level_six = 'level_six'
    level_seven = 'level_seven'
    level_eight = 'level_eight'
    level_nine = 'level_nine'
    level_ten = 'level_ten'
    level_eleven = 'level_eleven'
    level_twelve = 'level_twelve'
    level_thirteen = 'level_thirteen'
    level_fourteen = 'level_fourteen'
    level_fifteen = 'level_fifteen'
    level_choices = (
        (level_one, 'level_one'),
        (level_two, 'level_two'),
        (level_three, 'level_three'),
        (level_four, 'level_four'),
        (level_five, 'level_five'),
        (level_six, 'level_six'),
        (level_seven, 'level_seven'),
        (level_eight, 'level_eight'),
        (level_nine, 'level_nine'),
        (level_ten, 'level_ten'),
        (level_eleven, 'level_eleven'),
        (level_twelve, 'level_twelve'),
        (level_thirteen, 'level_thirteen'),
        (level_fourteen, 'level_fourteen'),
        (level_fifteen, 'level_fifteen'),
    )

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='single_leg_profile',primary_key=True)
    level = models.CharField(max_length=25, choices=level_choices, default=None)
    date = models.DateField(auto_now_add=False, null=True, blank=True)
    ammount = models.BigIntegerField(blank=True, null=True)
    remaining = models.BigIntegerField(blank=True, null=True)
    upgrade = models.IntegerField(blank=True, null=True) 
    withdrawl_ammount = models.BigIntegerField(blank=True, null=True)
    paid = models.BooleanField(default=False)
    withdrawl_bill = models.ForeignKey('WithdrawlBill', on_delete=models.CASCADE, related_name='withdrawl_bill', null=True, blank=True)

    def __str__(self):
        return str(self.profile) + ' - ' + self.level


class DirectSponsorIncome(models.Model):
    level_one = 'level_one'
    level_two = 'level_two'
    level_three = 'level_three'
    level_four = 'level_four'
    level_five = 'level_five'
    level_six = 'level_six'
    level_seven = 'level_seven'
    level_eight = 'level_eight'
    level_nine = 'level_nine'
    level_ten = 'level_ten'
    direct_level_choices = (
        (level_one, 'level_one'),
        (level_two, 'level_two'),
        (level_three, 'level_three'),
        (level_four, 'level_four'),
        (level_five, 'level_five'),
        (level_six, 'level_six'),
        (level_seven, 'level_seven'),
        (level_eight, 'level_eight'),
        (level_nine, 'level_nine'),
        (level_ten, 'level_ten'))
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='direct_profile')
    level = models.CharField(max_length=25, choices=direct_level_choices, default=None)
    users = models.ManyToManyField(Profile, related_name='level_user')
    total_users = models.IntegerField(blank=True, null=True)
    remaining = models.BigIntegerField(blank=True, null=True)
    ammount = models.BigIntegerField(blank=True, null=True)
    withdrawl_ammount = models.BigIntegerField(blank=True, null=True)
    withdrawl_bill = models.ForeignKey('WithdrawlBill', on_delete=models.CASCADE, related_name='direct_level_withdrawl_bill', blank=True, null=True)
    def __str__(self):
        return str(self.profile) + ' - ' + self.level

class RoyaltyIncome(models.Model):
    level_one = 'level_one'
    level_two = 'level_two'
    level_three = 'level_three'
    royalty_coices = (
        (level_one, 'level_one'),
        (level_two, 'level_two'),
        (level_three, 'level_three'),
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='royalty_profile')
    level = models.CharField(max_length=25, choices=royalty_coices, default=None)
    ammount = models.BigIntegerField(blank=True, null=True)
    withdrawl_ammount = models.BigIntegerField(blank=True, null=True)
    remaining = models.BigIntegerField(blank=True, null=True)
    withdrawl_bill = models.ForeignKey('WithdrawlBill', on_delete=models.CASCADE, related_name='royalty_income_withdrawl_bill', blank=True, null=True)

    def __str__(self):
        return str(self.profile) + ' - ' + self.level

class WithdrawlBill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    single_leg = models.ForeignKey('SingleLegIncome', on_delete=models.CASCADE, blank=True, null=True)
    royalty = models.ForeignKey('RoyaltyIncome', on_delete=models.CASCADE, blank=True, null=True)
    direct = models.ForeignKey('DirectSponsorIncome', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(unique=True, auto_now_add=True, blank=True, null=True)
    ammount = models.BigIntegerField(null=True, blank=True)
    method = models.CharField(max_length=150, null=True, blank=True)
    request = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    paid_method = models.CharField(blank=True, null=True, max_length=150)
    paid_by = models.CharField(blank=True, null=True, max_length=150)
    paid_date = models.DateTimeField(auto_created=False, blank=True, null=True)
    def __str__(self):
        return str(self.profile) + ' - ' + self.date.strftime('%m/%d/%Y')

class GrandTotal(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, blank=True, null=True)
    total = models.BigIntegerField(null=True, blank=True, default = 0)
    withdrawn = models.BigIntegerField(blank=True, null = True, default = 0)
    remaining = models.BigIntegerField(null=True, blank=True, default = 0)
    def __str__(self):
        return str(self.profile)
