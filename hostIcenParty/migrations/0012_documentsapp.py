# Generated by Django 2.2.14 on 2020-09-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostIcenParty', '0011_auto_20200903_0327'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentsApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file_img_document', models.FileField(blank=True, null=True, upload_to='documents/documents/')),
            ],
        ),
    ]
