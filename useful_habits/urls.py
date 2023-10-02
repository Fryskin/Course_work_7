from django.urls import path
from useful_habits.apps import UsefulHabitsConfig

from useful_habits.views import UsefulHabitCreateAPIView, UsefulHabitListAPIView, UsefulHabitRetrieveAPIView,\
                                UsefulHabitUpdateAPIView, UsefulHabitDestroyAPIView


app_name = UsefulHabitsConfig.name

urlpatterns = [
    path('useful_habit/create/', UsefulHabitCreateAPIView.as_view(), name='useful_habit_create'),
    path('useful_habits/', UsefulHabitListAPIView.as_view(), name='useful_habits_list'),
    path('useful_habit/<int:pk>', UsefulHabitRetrieveAPIView.as_view(), name='useful_habit_view'),
    path('useful_habit/update/<int:pk>', UsefulHabitUpdateAPIView.as_view(), name='useful_habit_update'),
    path('useful_habit/delete/<int:pk>', UsefulHabitDestroyAPIView.as_view(), name='useful_habit_delete'),
]
