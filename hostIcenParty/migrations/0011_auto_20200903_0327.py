# Generated by Django 2.2.14 on 2020-09-03 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostIcenParty', '0010_auto_20200903_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyproduct',
            name='status_buy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostIcenParty.StatusBuy'),
        ),
    ]