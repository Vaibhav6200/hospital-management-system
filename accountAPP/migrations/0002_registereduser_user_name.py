# Generated by Django 3.2.4 on 2021-06-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registereduser',
            name='user_name',
            field=models.CharField(default=23, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]