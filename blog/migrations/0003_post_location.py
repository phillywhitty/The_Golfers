# Generated by Django 3.2.21 on 2023-10-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]