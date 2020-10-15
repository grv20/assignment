from django.urls import path
from .views import personApi

urlpatterns = [
    path('person/',personApi),
    path('person/<int:id>',personApi)
]