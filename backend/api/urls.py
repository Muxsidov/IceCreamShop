from django.urls import path

from . import views

urlpatterns = [
    path('', views.IceCreamListAPIView.as_view()),
    path('<int:pk>/', views.IceCreamDetailAPIView.as_view()),
    path('create/', views.IceCreamCreateAPIView.as_view()),
    path('<int:pk>/delete/', views.IceCreamDestroyAPIView.as_view()),
    path('<int:pk>/update/', views.IceCreamUpdateAPIView.as_view())
]