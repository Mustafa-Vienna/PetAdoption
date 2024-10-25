from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="main-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SelectedPostView.as_view(),
         name="post-detail-page"),
    path("testimonials", views.testimonials_page, name="testimonials-page"),
    path("create_post", views.CreatePost.as_view(), name="create-post")
]
