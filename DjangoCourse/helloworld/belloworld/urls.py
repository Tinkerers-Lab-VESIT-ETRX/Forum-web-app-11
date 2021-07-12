from django.urls import path
from belloworld import views
urlpatterns = [
    path('',views.belloworld, name='belloworld'),
]
