from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Post class in admin panel
    """
    list_display = ('title','slug', 'published_on')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'published_on')
    summernote_fields = ('description', 'ingredients', 'preparation_steps')
   


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'published_on', 'approved')
    list_filter = ('approved', 'published_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)