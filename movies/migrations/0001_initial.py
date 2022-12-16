# Generated by Django 3.2.16 on 2022-12-16 18:39

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('genre', models.CharField(blank=True, choices=[('NP', 'No Preference'), ('ACT', 'Action'), ('ADV', 'Adventure'), ('COM', 'Comedy'), ('CRI', 'Crime'), ('DRA', 'Drama'), ('FAM', 'Family'), ('FAN', 'Fantasy'), ('HOR', 'Horror'), ('MUS', 'Music'), ('ROM', 'Romance'), ('SCI', 'Sci-Fi'), ('SPT', 'Sport'), ('SUP', 'Superhero'), ('THR', 'Thriller'), ('WAR', 'War'), ('WST', 'Western')], default='', max_length=50)),
                ('release_date', models.DateField()),
                ('director', models.CharField(max_length=50)),
                ('age_rating', models.IntegerField()),
                ('summary', models.TextField(max_length=1000)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder_image', max_length=255, verbose_name='movie_image')),
                ('average_stars', models.FloatField()),
            ],
        ),
    ]
