# Generated by Django 2.2.14 on 2020-09-04 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostIcenParty', '0012_documentsapp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentsapp',
            old_name='file_img_document',
            new_name='file_document',
        ),
    ]