# Generated by Django 3.0.2 on 2020-08-17 17:52

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('star', '0003_auto_20200817_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='publish',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата'),
        ),
        migrations.AlterUniqueTogether(
            name='posts',
            unique_together={('author', 'publish')},
        ),
    ]
