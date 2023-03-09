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


    
class RecipeDetail(View):
    """ Recipe details page """

    def get(self, request, slug):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        #comments = Comment.objects.all(post__id=post.id).order_by('published_on')
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
                "liked": liked,
                "comment_form": CommentForm()
            }
        )
