# Generated by Django 3.0.8 on 2021-06-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210619_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(blank=True, max_length=255, verbose_name='Image URL'),
        ),
    ]