# Generated by Django 2.2.5 on 2021-06-09 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'verbose_name': '应聘者', 'verbose_name_plural': '应聘者'},
        ),
    ]