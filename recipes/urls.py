from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostRecipe.as_view(), name='home'),
    path('<slug:slug>/', views.PostRecipe.as_view(), name='post_recipe'),
]