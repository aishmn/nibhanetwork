# Generated by Django 2.1.4 on 2019-01-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20190114_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nominee_aadhar_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nominee_dob',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nominee_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nominee_relation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
