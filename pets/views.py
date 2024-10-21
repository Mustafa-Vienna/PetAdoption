from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.


def index_page(request):
    fresh_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "pets/index.html", {
        "posts": fresh_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "pets/posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    selected_post = get_object_or_404(Post, slug=slug)
    return render(request, "pets/post-detail.html", {
        "post": selected_post,
        "post_tags": selected_post.tags.all()
    })


def testimonials_page(request):
    pass
