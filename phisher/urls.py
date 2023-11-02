from django.urls import path

from .views import secret

urlpatterns = [
    path('super-secret', secret, name="secret"),
]
