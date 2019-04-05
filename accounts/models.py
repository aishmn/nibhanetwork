from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from PIL import Image
from django.utils.timezone import now
from django.contrib import messages

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')
    activated = models.BooleanField(default=False)
    activated_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    full_name = models.CharField(max_length=250, blank=True)
    refered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='refered_by', blank=True, null=True)
    permanent_address = models.CharField(max_length=250, blank=True)
    user_contact_no= models.BigIntegerField(null=True, blank=True)
    user_bank_name = models.CharField(max_length=250, blank=True)
    user_bank_address = models.CharField(max_length=250, blank=True )
    user_bank_ac_no = models.BigIntegerField(null=True, blank=True)
    user_bank_IFSC = models.CharField(max_length=250,blank=True)
    user_profile_image = models.ImageField(upload_to='nhpluser/nhpluser_profile_image', height_field=None, width_field=None, max_length=None, blank=True)
    pan_card_no = models.CharField(max_length=250, blank=True)
    aadhar_card_no = models.BigIntegerField(null=True, blank=True)
    aadhar_card_image = models.ImageField(upload_to='nhpluser/aadhar_card_image', height_field=None, blank=True, width_field=None, max_length=None)
    pan_card_image = models.ImageField(upload_to='nhpluser/user_pan_card_image', height_field=None, width_field=None, max_length=None, blank=True)
    pass_book_image = models.ImageField(upload_to='nhpluser/passbook_image', height_field=None, width_field=None, max_length=None, blank=True)
    cancel_cheque = models.ImageField(upload_to='nhpluser/cancel_cheque_image', height_field=None, width_field=None, max_length=None, blank=True)
    bhim_upi =  models.BigIntegerField(null=True, blank=True)
    paypal =  models.BigIntegerField(null=True, blank=True)
    googlepay = models.BigIntegerField(null=True, blank=True)
    paytm =  models.BigIntegerField(null=True, blank=True)
    phonepay = models.BigIntegerField(null=True,blank=True)
    sponsored_user = models.ManyToManyField(User, related_name='sponsored_user')
    nominee_name = models.CharField(max_length = 100, blank=True, null=True)
    nominee_dob = models.DateTimeField(auto_now = False, auto_now_add = False, blank=True, null=True)
    nominee_relation = models.CharField(max_length = 100, blank=True, null=True)
    nominee_aadhar_no = models.CharField(max_length = 100, blank=True, null=True)
    def __str__(self):
        return str(self.user)