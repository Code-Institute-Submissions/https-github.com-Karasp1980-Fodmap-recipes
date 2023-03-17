from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm




class HomePage(generic.ListView):
    """
    all_recipes view
    """
    model = Post
    queryset = Post.objects.order_by('-published_on')
    template_name = 'index.html'
    paginate_by = 6


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
            return redirect('')
        else:
            messages.error(self.request, 'Please complete all required fields')
            recipe_form = RecipeForm()

        return render(
            request,
            "add_recipe.html",
            {
                "recipe_form": recipe_form

            },
        )        
