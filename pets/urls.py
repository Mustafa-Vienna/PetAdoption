from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_page, name="main-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
    path("testimonials", views.testimonials_page, name="testimonials-page")
]
