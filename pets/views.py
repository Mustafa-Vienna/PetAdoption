from django.shortcuts import render


# Create your views here.


def index_page(request):
    return render(request, "pets/index.html")


def posts_page(request):
    pass


def post_detail(requests):
    pass
