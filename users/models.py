from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    st = (
        ("м", "муж."),
        ("ж", "жен."),

    )
    user = models.OneToOneField(User,
        on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True,verbose_name="Дата рождения")
    time_of_birth=models.TimeField(blank=True, null=True,verbose_name="Время рождения")
    city1=models.CharField(max_length=20,blank=True, null=True,verbose_name='Место рождения')
    city2 = models.CharField(max_length=20, blank=True, null=True,verbose_name="Место проживания")
    gender=models.CharField(max_length=5,choices=st,verbose_name="Пол")
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True,verbose_name="Ваше фото")

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
