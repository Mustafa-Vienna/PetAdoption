from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post

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


class SelectedPostView(DetailView):
    template_name = "pets/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context


def testimonials_page(request):
    pass
