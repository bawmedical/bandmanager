# Generated by Django 4.0.6 on 2022-07-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandapp', '0003_alter_song_key_alter_song_original_artist_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('location', models.CharField(blank=True, default='', max_length=300)),
                ('twitter', models.CharField(blank=True, default='', max_length=300)),
            ],
        ),
    ]
