# Generated by Django 2.2.3 on 2019-07-27 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190727_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.UserProfile'),
        ),
    ]