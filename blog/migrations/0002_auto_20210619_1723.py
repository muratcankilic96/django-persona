# Generated by Django 3.0.8 on 2021-06-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=255, verbose_name='Image URL'),
        ),
    ]
