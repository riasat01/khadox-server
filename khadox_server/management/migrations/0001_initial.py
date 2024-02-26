# Generated by Django 5.0.2 on 2024-02-22 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image_url', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=255)),
                ('restaurant_address', models.CharField(max_length=255)),
                ('cover_photo', models.URLField(max_length=255)),
                ('ratings', models.FloatField(default=0.0)),
                ('number_of_raters', models.PositiveIntegerField(default=0)),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.district')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
                ('food_image', models.URLField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('ratings', models.FloatField(default=0.0)),
                ('number_of_raters', models.PositiveIntegerField(default=0)),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.restaurant')),
            ],
        ),
    ]