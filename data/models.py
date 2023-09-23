from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class Product(models.Model):

    owner = models.CharField(max_length=30, verbose_name='Владелец')
    title = models.CharField(max_length=50, verbose_name='Название курса')

    class Meta:
        ordering = ('owner', 'title')
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'

    def __str__(self):
        return self.title


class Student(AbstractUser):
    products = models.ManyToManyField(Product, related_name='products')
    username = models.CharField(
        max_length=40,
        verbose_name='Ник',
        unique=True,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+$',
            message='Имя пользователя содержит недопустимый символ'
        )]
    )
    email = models.EmailField(
        max_length=50,
        verbose_name='email',
    )

    class Meta:
        ordering = ('username', )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    url = models.URLField()
    viewing = models.IntegerField(verbose_name='Продолжительность')
    product = models.ForeignKey(Product,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='lessons'
                                )
    student_time = models.ManyToManyField(Student, through='TimeInfo')

    class Meta:
        ordering = ('title', )
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.title


class TimeInfo(models.Model):
    student = models.ForeignKey(Student,
                                on_delete=models.CASCADE,
                                related_name='student'
                                )
    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE,
                               related_name='lesson'
                               )
    viewing_duration = models.IntegerField(
        verbose_name='Продолжительность просмотра'
        )
    viewing_time = models.TimeField(verbose_name='Время просмотра')

    class Meta:
        ordering = ('viewing_time', )
        verbose_name = 'Время просмотра'
        verbose_name_plural = 'Время просмотров'

    def __str__(self):
        return (f'{self.student.username} посмотрел {self.viewing_time} секунд'
                f' из {self.lesson.title}'
                )
