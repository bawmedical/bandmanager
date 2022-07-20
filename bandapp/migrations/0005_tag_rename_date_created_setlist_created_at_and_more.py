# Generated by Django 4.0.6 on 2022-07-20 09:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bandapp', '0004_band'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='setlist',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='setlist',
            old_name='date_updated',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='date_updated',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='band',
            name='bandcamp',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='band',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='band',
            name='facebook',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='band',
            name='instagram',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='band',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='band',
            name='soundcloud',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='band',
            name='youtube',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='setlist',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='song',
            name='chart_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='song',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='song',
            name='video_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='setlist',
            name='songs',
            field=models.ManyToManyField(blank=True, related_name='setlists', to='bandapp.song'),
        ),
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(max_length=300)),
                ('setlist', models.ManyToManyField(blank=True, to='bandapp.setlist')),
                ('tags', models.ManyToManyField(blank=True, related_name='gigs', to='bandapp.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='band',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='bands', to='bandapp.tag'),
        ),
        migrations.AddField(
            model_name='setlist',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='setlists', to='bandapp.tag'),
        ),
        migrations.AddField(
            model_name='song',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='songs', to='bandapp.tag'),
        ),
    ]
