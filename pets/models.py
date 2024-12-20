from django.db import models
from django.core.validators import (
    MaxLengthValidator,
    MinValueValidator,
    MaxValueValidator
)
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.utils.text import slugify
# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=25)
    """
    Represents a tag that can be associated with posts
    """

    def __str__(self):
        """
        Return the tag caption as its string representation
        """
        return self.caption


class Author(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    """
    Represents a post with details about a pet, including:
    title, name, age, excerpt, image, content, author, tags, and likes
    """
    title = models.CharField(max_length=50, unique=True)
    pet_name = models.CharField(max_length=100)
    pet_age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)])
    excerpt = models.CharField(max_length=200)
    image = CloudinaryField('image', folder="posts")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True, blank=True)
    content = models.TextField(validators=[MaxLengthValidator(700)])
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

    def save(self, *args, **kwargs):
        """
        Auto generate a unique slug based on the title
        """
        if not self.slug:
            user_slug = slugify(self.title)
            slug = user_slug
            unique_slug_counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{user_slug} - {unique_slug_counter}"
                unique_slug_counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def clean(self):
        """
        Validate the post before saving, ensures the title is not too long
        """
        super().clean()
        if len(self.title) > 50:
            raise ValidationError(
                "Oops! The title you entered is too long. "
                "Please limit it to 50 characters.")

    def __str__(self):
        """
        Return the post title as its string representation
        """
        return self.title

    def total_likes(self):
        """
        Return the total count of likes for the post
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Represents a comment on a post with
    author, comment text and creation time
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(max_length=600)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return a brief string representation of the comment
        """
        return f"Comment by {self.author.username} on {self.text[:30]}"
