from django import forms
from useful_habits.models import UsefulHabit


class UsefulHabitForm(forms.ModelForm):
    class Meta:
        model = UsefulHabit
        fields = '__all__'
