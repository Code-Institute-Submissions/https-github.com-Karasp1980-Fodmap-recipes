""" Test for views.py """
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class TestUser(TestCase):
    """ user """
    def test_user(self):
        """ user """
        test_user = User.objects.create_user(
            username='testuser', password='654321'
            )
        self.post = Post.objects.create(title='Test', author=test_user)
        self.comment = Comment.objects.create(
            body='Test Comment', post=self.post
            )
        self.client.login(username="testuser", password="654321")


class TestGetPages(TestCase):
    """ test to ensure that all the pages display"""
    def test_get_home_page(self):
        """
        Home page 
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    def test_get_about_page(self):
        """
        About Fodmaps page
        """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')



    def test_get_all_recipes_page(self):
        """
        All recipes page
        """
        response = self.client.get('/all_recipes')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_recipes.html')

    def test_get_fav_recipes_page(self):
        """
        Favourite recipes page
        """
        response = self.client.get('/favourite_recipes')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favourite_recipes.html')

    def test_get_my_recipes_page(self):
        """
        My recipes page
        """
        response = self.client.get('/my_recipes')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_recipes.html')

    def test_get_add_recipes_page(self):
        """
        Add recipes page
        """
        response = self.client.get('/add_recipe')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')

    def test_recipe_details_page(self):
        """
        Recipe details page
        """
        posts = Post.objects.all()
        for post in posts:
            response = self.client.get(f'/recipe_details/{self.post.id}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'recipe_details.html')

    def test_edit_recipe_page(self):
        """
        Edit recipe page 
        """
        posts = Post.objects.all()
        for post in posts:
            response = self.client.get(f'/edit_recipe/{self.post.id}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'edit_recipe.html')

    def test_delete_recipe_page(self):
        """
        Delete recipe page 
        """
        posts = Post.objects.all()
        for post in posts:
            response = self.client.get(f'/delete_recipe/{self.post.id}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'delete_recipe.html')


    def test_edit_comment_page(self):
        """
        Edit comment page 
        """
        comments = Comment.objects.all()
        for comment in comments:
            response = self.client.get(f'/edit_comment/{self.comment.id}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'edit_comment.html')

    def test_delete_comment_page(self):
        """
        Delete comment page 
        """
        comments = Comment.objects.all()
        for comment in comments:
            response = self.client.get(f'/delete_comment/{self.comment.id}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'delete_comment.html')


    def test_search_page(self):
        """
        Search page 
        """
        response = self.client.get('/search')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')




