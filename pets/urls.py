from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_page, name="main-page"),

    path("testimonials", views.testimonials_page, name="testimonials-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
]
