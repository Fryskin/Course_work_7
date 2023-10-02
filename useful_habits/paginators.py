from rest_framework.pagination import PageNumberPagination


class UsefulHabitPaginator(PageNumberPagination):
    page_size = 5
