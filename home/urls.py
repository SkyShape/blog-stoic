from django.urls import path
from home import views


urlpatterns = [
    path('home/', views.HomeTemplateView.as_view(), name='home')
]
