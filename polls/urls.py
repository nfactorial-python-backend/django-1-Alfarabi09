from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:first>/add/<int:second>/', views.add, name='add'),
    path('transform/<str:text>/', views.upp, name='upp'),
    path('check/<str:word>/', views.is_palindrome, name='is_palindrome'),
    path('calc/<int:first>/<str:operation>/<int:second>/', views.calculator, name='calculator'),
    path('randomnumber/<int:min>/<int:max>/', views.generate_random_number, name='random'),
    path('reverse/<str:text>/', views.reverse_text),
    path('factorial/<int:number>/', views.calculate_factorial),
]
