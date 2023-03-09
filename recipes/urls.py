
from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]