# Generated by Django 3.2.16 on 2022-12-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_profile_favourite_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favourite_genre',
            field=models.CharField(blank=True, choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Family', 'Family'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Music', 'Music'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'), ('Sport', 'Sport'), ('Superhero', 'Superhero'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], default='', max_length=50),
        ),
    ]
