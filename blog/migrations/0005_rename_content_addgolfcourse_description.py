# Generated by Django 3.2.24 on 2024-03-04 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20240303_2214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addgolfcourse',
            old_name='content',
            new_name='description',
        ),
    ]
