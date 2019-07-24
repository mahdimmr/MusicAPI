# Generated by Django 2.2.3 on 2019-07-24 14:16

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='cover',
            field=models.ImageField(upload_to=music.models.rename_cover),
        ),
        migrations.AlterField(
            model_name='music',
            name='file',
            field=models.FileField(upload_to=music.models.rename_music),
        ),
    ]