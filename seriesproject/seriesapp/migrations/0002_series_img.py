# Generated by Django 5.0.3 on 2024-04-11 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seriesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='img',
            field=models.ImageField(default='abcd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
