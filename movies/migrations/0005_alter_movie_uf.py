# Generated by Django 4.1.4 on 2022-12-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0004_movie_uf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="uf",
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]