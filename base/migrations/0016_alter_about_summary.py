# Generated by Django 3.2.4 on 2021-07-26 14:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_about_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='summary',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]