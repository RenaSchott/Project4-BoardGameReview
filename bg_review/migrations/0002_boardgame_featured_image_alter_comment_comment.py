# Generated by Django 4.2.11 on 2024-04-01 18:25

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bg_review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgame',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='bg_review.review'),
        ),
    ]
