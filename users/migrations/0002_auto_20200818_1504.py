# Generated by Django 3.0.2 on 2020-08-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.AddField(
            model_name='profile',
            name='city1',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Место рождения'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Место проживания'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('м', 'муж.'), ('ж', 'жен.')], max_length=5, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/', verbose_name='Ваше фото'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='time_of_birth',
            field=models.TimeField(blank=True, null=True, verbose_name='Время рождения'),
        ),
    ]
