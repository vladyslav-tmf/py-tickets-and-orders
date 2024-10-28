# Generated by Django 4.0.2 on 2024-10-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_alter_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AddIndex(
            model_name='movie',
            index=models.Index(fields=['title'], name='db_movie_title_5d0841_idx'),
        ),
    ]
