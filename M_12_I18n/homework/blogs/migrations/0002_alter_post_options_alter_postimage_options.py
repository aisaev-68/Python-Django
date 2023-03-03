# Generated by Django 4.1.7 on 2023-03-03 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['title', 'description'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='postimage',
            options={'ordering': ['post'], 'verbose_name': 'PostImage', 'verbose_name_plural': 'PostImages'},
        ),
    ]