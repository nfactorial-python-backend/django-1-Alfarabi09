from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:first>/add/<int:second>/', views.add, name='add'),
    path('transform/<str:text>/', views.upp, name='upp'),
]
