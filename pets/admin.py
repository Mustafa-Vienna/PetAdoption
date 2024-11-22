from django.contrib import admin
from .models import Post, Author, Tag, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    """
    Admin settings for the post model:
    filters, display fields, and slug generation
    """
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    """
    Admin settings for the comment model:
    Display author username and post in the admin list view
    """
    list_display = ("author_username", "post")

    def author_username(self, user):
        """
        Get the username of the comment's author.
        """
        return user.author.username


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
