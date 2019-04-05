from epin.models import Epin
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UserRegisterForm(UserCreationForm):
    mobile_no = forms.IntegerField(required=True)
    referror = forms.CharField(max_length=200, required=True)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'referror', 'mobile_no'] 


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'full_name',
            'permanent_address', 
            'user_contact_no', 
            'user_bank_name', 
            'user_bank_address', 
            'user_bank_ac_no', 
            'user_bank_IFSC', 
            'user_profile_image', 
            'pan_card_no',
            'aadhar_card_no',
            'aadhar_card_image',
            'pan_card_image',
            'pass_book_image',
            'cancel_cheque',
            'bhim_upi',
            'paypal',
            'paytm',
            'phonepay',
        ]

class EpinCreationForm(forms.ModelForm):
    class Meta:
        model = Epin
        fields = ('serial_no',)

class EpinActivationForm(forms.Form):
    pass 