# Generated by Django 3.2.24 on 2024-02-28 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_golfcourse_created_on'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
