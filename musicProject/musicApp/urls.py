from django.urls import path

from . import views

urlpatterns = [
    path('', views.music),
    path('shreya/', views.shreyaFunction),
    path('rehman/', views.rehmanFunction),
    path('alka/', views.alkaFunction),
]