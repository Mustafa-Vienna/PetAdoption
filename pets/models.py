from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=25)

    def __str__(self):
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
    title = models.CharField(max_length=100)
    pet_name = models.CharField(max_length=40)
    pet_age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(15)])
    excerpt = models.CharField(max_length=150)
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(15)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    # created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"Comment by {self.username} on {self.post}"
