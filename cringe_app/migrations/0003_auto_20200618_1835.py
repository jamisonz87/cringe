# Generated by Django 3.0.7 on 2020-06-18 22:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cringe_app', '0002_thread_thread_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
