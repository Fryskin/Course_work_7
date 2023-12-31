
from rest_framework import generics
from useful_habits.models import UsefulHabit
from useful_habits.paginators import UsefulHabitPaginator
from useful_habits.permissions import IsOwner, IsAuthenticated
from useful_habits.serializers import UsefulHabitSerializer


class UsefulHabitCreateAPIView(generics.CreateAPIView):
    """ Create a useful habit """
    serializer_class = UsefulHabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_useful_habit = serializer.save()
        new_useful_habit.save()


class UsefulHabitListAPIView(generics.ListAPIView):
    """ List created useful habits """
    serializer_class = UsefulHabitSerializer
    permission_classes = [IsOwner]
    pagination_class = UsefulHabitPaginator
    queryset = UsefulHabit.objects.all()
    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(owner=self.request.user)
    #     return queryset


class UsefulHabitPublicListAPIView(generics.ListAPIView):
    """ List created useful habits """
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]
    pagination_class = UsefulHabitPaginator


class UsefulHabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Retrieve the useful habit """
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()
    permission_classes = [IsAuthenticated]


class UsefulHabitUpdateAPIView(generics.UpdateAPIView):
    """ Update the useful habit """
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()
    permission_classes = [IsOwner]


class UsefulHabitDestroyAPIView(generics.DestroyAPIView):
    """ Delete the useful habit """
    queryset = UsefulHabit.objects.all()
    permission_classes = [IsOwner]
