from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from datetime import date

class Posts(models.Model):
    SHIRT_SIZES = (
        ('-2', 'Ужасно'),
        ('-1', 'Плохо'),
        ('0', 'Нормально'),
        ('1', 'Хорошо'),
        ('2', 'Отлично'),
    )
    st=(
        ("да","Да"),
        ("нет","Нет"),

    )
    size = models.CharField(max_length=5, choices=SHIRT_SIZES,db_index=True,verbose_name="Общая оценка")
    tags = TaggableManager(verbose_name="Облако тэгов")
    description=models.TextField(verbose_name="Описание")
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts',verbose_name="Автор")
    publish = models.DateField(default=date.today,verbose_name="Дата")
    status = models.CharField(max_length=5,
                              choices=st,
                              default='Да',verbose_name="Общий чат")

    class Meta:
        ordering = ('-publish',)

        unique_together = ['author', 'publish']

    def __str__(self):
        return self.description[0:10]
