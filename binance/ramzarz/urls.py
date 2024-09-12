from django.urls import path
from .views import MyAPI ,History

urlpatterns = [
    path('ramz/' ,MyAPI.as_view()),
    path('history/' ,History.as_view()),
]