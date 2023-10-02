
import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class UsefulHabit(models.Model):
    datatime_time_to_complete_the_habit = datetime.time(0, 2, 0)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='owner', **NULLABLE)
    location = models.CharField(max_length=200, verbose_name='location')
    time = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.datetime.now(), verbose_name='time')
    action = models.CharField(max_length=1000, verbose_name='action')
    is_pleasant = models.BooleanField(verbose_name='is pleasant')
    associated_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='associated habit', **NULLABLE)
    periodicity_in_hours = models.IntegerField(verbose_name='periodicity in hours')
    reward = models.CharField(max_length=300, verbose_name='reward', **NULLABLE)
    time_to_complete = models.TimeField(default=datatime_time_to_complete_the_habit, verbose_name='time_to_complete')
    is_public = models.BooleanField(verbose_name='is_public')

    def __str__(self):
        return f'UsefulHabit({self.action})'

    class Meta:
        verbose_name = 'useful_habit'
        verbose_name_plural = 'useful_habits'
        ordering = ('owner',)
