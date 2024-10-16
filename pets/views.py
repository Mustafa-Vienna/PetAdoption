from django.shortcuts import render


# Create your views here.


def index_page(request):
    return render(request, "pets/index.html")


def posts(request):
    return render(request, "pets/posts.html")


def testimonials_page(requests):
    pass


def post_detail(requests):
    pass
