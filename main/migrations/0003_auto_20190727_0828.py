# Generated by Django 2.2.3 on 2019-07-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190727_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]