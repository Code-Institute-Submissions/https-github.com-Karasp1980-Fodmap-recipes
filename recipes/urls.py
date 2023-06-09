from . import views
from django.urls import path
from .views import delete_comment, edit_comment


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('my_recipes', views.MyRecipes.as_view(), name='my_recipes'),
    path('favourite_recipes', views.FavouriteRecipes.as_view(),
         name='favourite_recipes'),
    path('all_recipes', views.AllRecipes.as_view(), name='all_recipes'),
    path('add_recipe', views.AddRecipe.as_view(), name='add_recipe'),
    path('edit_recipe/<int:pk>', views.EditRecipe.as_view(),
         name='edit_recipe'),
    path('delete_recipe/<int:pk>', views.DeleteRecipe.as_view(),
         name='delete_recipe'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_details'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('search', views.SearchRecipe.as_view(), name='search'),
    path('delete_comment/<int:id>/', views.delete_comment,
         name='delete_comment'),
    path('edit_comment/<int:pk>', views.edit_comment, name='edit_comment'),
]