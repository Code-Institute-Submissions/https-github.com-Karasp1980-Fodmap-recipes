from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm, RecipeForm
from django.utils.text import slugify
from django.views.generic.edit import UpdateView, DeleteView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib import messages


class HomePage(generic.ListView):
    """
    all_recipes view
    """
    model = Post
    queryset = Post.objects.order_by('-published_on')
    template_name = 'index.html'
    paginate_by = 8


class AboutPage(generic.TemplateView):
    """
    about view
    """
    template_name = 'about.html'


    
class RecipeDetails(View):
    """ Recipe details page """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = Comment.objects.filter(post__id=post.id).order_by('published_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )
        
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-published_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

class AllRecipes(generic.ListView):
    """
    all_recipes view
    """
    model = Post
    queryset = Post.objects.order_by('-published_on')
    template_name = 'all_recipes.html'
    paginate_by = 12

class MyRecipes(View):
    """ view for users recipes page"""

    def get(self, request):
        """your_recipes view, get method"""
        if request.user.is_authenticated:
            post = Post.objects.filter(author=request.user)

            paginator = Paginator(post, 8)  # 8 recipes per page showing
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(
                request, 'my_recipes.html', {"page_obj": page_obj, })
        else:
            return render(request, 'my_recipes.html')

class FavouriteRecipes(View):
    """ favourite recipes view"""
    def get(self, request):
        """favourite_recipes view, get method"""
        if request.user.is_authenticated:
            post = Post.objects.filter(likes=request.user.id)

            paginator = Paginator(post, 8)  # Show 8 recipes per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(
                request, 'favourite_recipes.html', {"page_obj": page_obj, })
        else:
            return render(request, 'favourite_recipes.html')

class AddRecipe(View):
    """ add recipe"""
    def get(self, request):
        """What happens for a GET request"""
        return render(
            request, "add_recipe.html", {"recipe_form": RecipeForm()})

    def post(self, request):
        """What happens for a POST request"""
        recipe_form = RecipeForm(request.POST, request.FILES)

        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify('-'.join([recipe.title,
                                            str(recipe.author)]),
                                  allow_unicode=False)
            recipe.save()
        
            return redirect('recipe_detail', recipe.slug)
        else:
            messages.error(self.request, 'Please complete all required fields')
            

        return render(
            request,
            "add_recipe.html",
            {
                "recipe_form": recipe_form

            },
        )  

class EditRecipe(UpdateView):
    """ Edit Recipe """
    model = Post
    template_name = 'edit_recipe.html'
    form_class = RecipeForm 
    success_url = "/my_recipes"

class DeleteRecipe(DeleteView):
    """ Delete Recipe """
    model = Post
    template_name = 'delete_recipe.html'
    success_url = "/my_recipes"    



class PostLike(View):
    
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_details', args=[slug]))


class SearchRecipe(View):
    """ Search recipes view"""

    def get(self, request):
        """get method"""
        return render(request, 'search.html')

    def post(self, request):
        """ post method"""
        searched = request.POST.get('searched')
        post = Post.objects.filter(title__icontains=searched)
        paginator = Paginator(post, 8)  # Show 8 recipes per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'searched': searched
        }
        return render(request, 'search.html', context)




class EditComment(UpdateView):
    """ Edits Comment """
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm
    success_url = "/"
   
    

class DeleteComment(DeleteView):
    """ Deletes Comment """
    model = Comment
    template_name = 'delete_comment.html'
    success_url = "/"
