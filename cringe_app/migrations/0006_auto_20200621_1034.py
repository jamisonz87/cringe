# Generated by Django 3.0.7 on 2020-06-21 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cringe_app', '0005_auto_20200619_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='message',
            field=models.TextField(default=''),
        ),
    ]