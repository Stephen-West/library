# Generated by Django 2.1.3 on 2018-11-24 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piece',
            name='code',
        ),
    ]
