from rest_framework import serializers
from useful_habits.models import UsefulHabit
from useful_habits.validators import TimeToCompleteValidation, AssociatedHabitValidation, \
    RewardAndAssociatedValidation, PleasantValidation, PeriodicityInHoursValidation


class UsefulHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulHabit
        fields = '__all__'
        validators = [TimeToCompleteValidation(field='time_to_complete'),
                      AssociatedHabitValidation(field='associated_habit'),
                      RewardAndAssociatedValidation(first_field='associated_habit', second_field='reward'),
                      PleasantValidation(first_field='is_pleasant', second_field='associated_habit',
                                         third_field='reward'),
                      PeriodicityInHoursValidation(field='periodicity_in_hours')
                      ]
