import datetime

from rest_framework.serializers import ValidationError

from useful_habits.models import UsefulHabit


class TimeToCompleteValidation:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        datatime_time_to_complete_the_habit = datetime.time(0, 2, 0)
        tmp_val = dict(value).get(self.field)

        if tmp_val is not None:
            if tmp_val > datatime_time_to_complete_the_habit:
                raise ValidationError('The time to complete the habit supposed to be less then 121 seconds.')


class AssociatedHabitValidation:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        habit = UsefulHabit.objects.filter(pk=tmp_val)

        if tmp_val is not None:
            if habit.is_pleasant is False:
                raise ValidationError('Only pleasant habits can be associated.')


class RewardAndAssociatedValidation:
    def __init__(self, first_field, second_field):
        self.first_field = first_field
        self.second_field = second_field

    def __call__(self, value):
        tmp_val_first_field = dict(value).get(self.first_field)
        tmp_val_second_field = dict(value).get(self.second_field)

        if tmp_val_first_field is not None and tmp_val_second_field is not None:
            raise ValidationError('It is impossible to define reward and associated habit simultaneously.')


class PleasantValidation:

    def __init__(self, first_field, second_field, third_field):
        self.first_field = first_field
        self.second_field = second_field
        self.third_field = third_field

    def __call__(self, value):
        tmp_val_first_field = dict(value).get(self.first_field)
        tmp_val_second_field = dict(value).get(self.second_field)
        tmp_val_third_field = dict(value).get(self.third_field)

        if tmp_val_first_field is True and tmp_val_second_field is not None or tmp_val_first_field is True and\
                tmp_val_third_field is not None:

            raise ValidationError('A pleasant habit cannot have a reward or an associated habit.')


class PeriodicityInHoursValidation:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)

        if tmp_val is not None:
            if tmp_val > 168:
                raise ValidationError('You cannot perform the habit less than once every 7 days.')
