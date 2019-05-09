# Generated by Django 2.1.3 on 2018-11-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_remove_piece_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='piece',
            name='number_of_copies',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='piece',
            name='parts',
            field=models.PositiveIntegerField(default=1),
        ),
    ]