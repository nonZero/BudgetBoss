from django.urls import path

from . import views

app_name = "expenses"

urlpatterns = [
    path('', views.expense_list, name="list"),
    path('add/', views.expense_create, name="create"),
    path('<int:pk>/',
         views.expense_detail,
         name="detail"),
]
