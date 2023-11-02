from django.urls import path

from  .views import users

urlpatterns = [
    path('super-secret', users, name="users"),
]