from django.contrib import admin

from useful_habits.forms import UsefulHabitForm
from useful_habits.models import UsefulHabit


@admin.register(UsefulHabit)
class UsefulHabitAdmin(admin.ModelAdmin):
    list_display = ('owner', 'location', 'time', 'action', 'is_pleasant', 'associated_habit', 'periodicity_in_hours',
                    'reward', 'time_to_complete', 'is_public',)
    list_filter = ('owner', 'is_pleasant', 'is_public')
    form = UsefulHabitForm
