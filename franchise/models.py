from django.db import models

# Create your models here.
class Franchise(models.Model):
    franchise_name = models.CharField(db_index=True, max_length=50)
    franchise_contact_no= models.BigIntegerField(blank=True,null=True)
    franchise_bank_name = models.CharField(max_length=50,blank=True,null=True)
    franchise_bank_address = models.CharField(max_length=50,blank=True,null=True)
    franchise_bank_ac_no = models.BigIntegerField(blank=True,null=True)
    franchise_bank_IFSC = models.CharField(max_length=50,blank=True,null=True)
    franchise_profile_image = models.ImageField(upload_to='franchise/franchise_profile_image/%Y/%m/%d',blank=True,null=True, height_field=None, width_field=None, max_length=None)
    pan_card_no = models.CharField(max_length=50,blank=True,null=True)
    aadhar_card_no = models.BigIntegerField(blank=True,null=True)
    aadhar_card_image = models.ImageField(upload_to='franchise/aadhar_card_image/%Y/%m/%d', height_field=None, width_field=None, max_length=None, blank=True,null=True)
    pan_card_image = models.ImageField(upload_to='franchise/franchise_pan_card_image/%Y/%m/%d', height_field=None, width_field=None, max_length=None, blank=True,null=True)
    pass_book_image = models.ImageField(upload_to='franchise/passbook_image/%Y/%m/%d', height_field=None, width_field=None, max_length=None, blank=True,null=True)
    cancel_cheque = models.ImageField(upload_to='franchise/cancel_cheque_image/%Y/%m/%d', height_field=None, width_field=None, max_length=None, blank=True,null=True)
    bhim_upi =  models.BigIntegerField(blank=True,null=True)
    paypal =  models.BigIntegerField(blank=True,null=True)
    paytm =  models.BigIntegerField(blank=True,null=True)
    phonepay = models.BigIntegerField(blank=True,null=True)
    class Meta:
        ordering = ('franchise_name', )
        verbose_name = 'Franchise'
        verbose_name_plural = 'Franchies'


    def __str__(self):
            return self.franchise_name