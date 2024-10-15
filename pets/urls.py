from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_page, name="main-page"),
    path("about", views.about_page, name="about-page"),
    path("testimonials", views.testimonials_page, name="testimonials-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
]
