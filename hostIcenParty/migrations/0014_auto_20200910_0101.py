# Generated by Django 2.2.14 on 2020-09-10 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostIcenParty', '0013_auto_20200904_1516'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('title',)},
        ),
    ]