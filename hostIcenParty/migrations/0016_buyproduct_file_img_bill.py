# Generated by Django 2.2.14 on 2020-09-10 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostIcenParty', '0015_buyproduct_is_finish'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyproduct',
            name='file_img_bill',
            field=models.FileField(blank=True, null=True, upload_to='documents/bill/'),
        ),
    ]
