# Generated by Django 2.1.3 on 2019-01-15 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20181216_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='original_ref',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
