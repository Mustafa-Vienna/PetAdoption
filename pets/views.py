from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post, Comment
from .forms import CommentForm, UserPostForm

# Create your views here.


class HomePageView(ListView):
    template_name = "pets/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    template_name = "pets/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


class SelectedPostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "pets/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "pets/post-detail.html", context)


class CreatePost(View):
    def get(self, request):
        form = UserPostForm()
        return render(request, 'pets/create-post.html', {
            'form': form
        })

    def post(self, request):
        form = UserPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main-page')
        return render(request, 'pets/create-post.html', {
            'form': form
        })


def testimonials_page(request):
    pass
