from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """
    Post model
    """
    title = models.CharField(max_length=200, blank=False, null=False, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    published_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    ingredients = models.TextField()
    preparation_steps = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ["-published_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["published_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def is_approved(self):
        return self.approved