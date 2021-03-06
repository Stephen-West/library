# Generated by Django 2.1.3 on 2018-11-29 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_piece_borrowed_from'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('first_names', models.CharField(blank=True, max_length=50, null=True)),
                ('suffix', models.CharField(blank=True, max_length=10, null=True)),
                ('dates', models.CharField(blank=True, max_length=30, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='piece',
            name='composed_by',
            field=models.ManyToManyField(to='music.Composer'),
        ),
    ]
