# Generated by Django 2.2.14 on 2020-09-02 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostIcenParty', '0004_buyproduct_objectproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyproduct',
            old_name='objectProduct',
            new_name='file_img_home',
        ),
    ]