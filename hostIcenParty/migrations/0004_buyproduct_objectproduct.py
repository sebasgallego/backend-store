# Generated by Django 2.2.14 on 2020-09-02 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostIcenParty', '0003_buyproduct_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyproduct',
            name='objectProduct',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
