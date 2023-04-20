from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm, RecipeForm
from django.utils.text import slugify
from django.views.generic.edit import UpdateView, DeleteView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Count


class HomePage(generic.ListView):
    """
    all_recipes view
    """
    model = Post
    queryset = Post.objects.order_by('-published_on')
    template_name = 'index.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['liked_recipes'] = Post.objects.annotate(
         num_likes=Count('likes')
        ).order_by('-num_likes')
        for post in context['object_list']:
            post.comment_count = post.comments.filter(approved=True).count()
        return context


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
        comments = Comment.objects.filter(
         post__id=post.id
        ).order_by('published_on')
        post.comment_count = post.comments.filter(approved=True).count()
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
        comments = post.comments.filter(
         approved=True
        ).order_by("-published_on")
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for post in context['object_list']:
            post.comment_count = post.comments.filter(approved=True).count()
        return context


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
            post = list(Post.objects.filter(likes=request.user.id))
            paginator = Paginator(post, 8)  # Show 8 recipes per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            for post in post:
                post.comment_count = post.comments.filter(
                 approved=True
                ).count()
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
            messages.success(request, "Recipe added successfully")
            return redirect('recipe_details', recipe.slug)
        else:
            messages.error(self.request, 'Please complete all required fields')

        return render(
            request,
            "add_recipe.html",
            {
                "recipe_form": recipe_form
            },)


class EditRecipe(UpdateView):
    """ Edit Recipe """
    model = Post
    template_name = 'edit_recipe.html'
    form_class = RecipeForm
    success_url = "/my_recipes"

    def form_valid(self, form):
        messages.success(self.request, "Recipe edited successfully")
        return super().form_valid(form)


class DeleteRecipe(DeleteView):
    """ Delete Recipe """
    model = Post
    template_name = 'delete_recipe.html'
    success_url = "/my_recipes"

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Recipe deleted successfully")
        return super().delete(request, *args, **kwargs)


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
        post_with_title = Post.objects.filter(title__icontains=searched)
        post_with_ingredient = Post.objects.filter(
            ingredients__icontains=searched
        )
        # Combines the two query results
        posts = post_with_title | post_with_ingredient
        for post in posts:
            if post:
                post.comment_count = post.comments.filter(
                    approved=True
                    ).count()
            else:
                post.comment_count = 0
            print(post.comment_count)
        paginator = Paginator(posts, 8)  # Show 8 recipes per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'searched': searched,
            'post': posts,
            }

        return render(request, 'search.html', context)


def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment edited successfully")
            return redirect('recipe_details', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)
        context = {'form': form, 'comment': comment}
    return render(request, 'edit_comment.html', context)


def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    post = get_object_or_404(Post, id=comment.post.id)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, "Comment deleted successfully")
        return redirect(reverse('recipe_details', args=[post.slug]))
    return render(
     request,
     'delete_comment.html',
     {'comment': comment, 'post': post}
    )