# Generated by Django 4.0.5 on 2022-06-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_file_downloads'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='max_downloads',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='file',
            name='size',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
