# Generated by Django 4.2.7 on 2023-11-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_comment_user_remove_post_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('The K Club', 'The K Club'), ('Ballybunnion', 'Ballybunnion'), ('The Abbey', 'The Abbey')], default='Unknown', max_length=20),
        ),
    ]