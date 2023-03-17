
from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_detail'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
]