# Generated by Django 4.0.5 on 2022-06-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='filename',
            field=models.CharField(default='nepomenovany', max_length=128),
            preserve_default=False,
        ),
    ]
