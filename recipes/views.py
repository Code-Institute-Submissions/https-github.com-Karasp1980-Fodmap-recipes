from django.shortcuts import render
from django.views import generic, View
from .models import Post


class PostRecipe(generic.ListView):
    """
    all_recipes view
    """
    model = Post
    queryset = Post.objects.order_by('-published_on')
    template_name = 'index.html'
    paginate_by = 6

    
class RecipeDetails(View):
    """ Recipe details page """

    def get(self, request, slug):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments_post_name.order_by('published_on')
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
