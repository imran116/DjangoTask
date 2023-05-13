from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeView.as_view()),
    path('contact/', views.ContactView.as_view(), name='contact'),
]