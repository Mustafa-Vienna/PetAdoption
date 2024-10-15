from django.shortcuts import render


# Create your views here.


def index_page(request):
    return render(request, "pets/index.html")


def about_page(request):
    pass


def testimonials_page(requests):
    pass


def post_detail(requests):
    pass
