from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="main-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SelectedPostView.as_view(),
         name="post-detail-page"),
    path("create_post", views.PostCreateView.as_view(), name="create-post"),
    path("posts/<slug:slug>/delete/",
         views.PostDeleteView.as_view(), name="delete-post"),
    path("posts/<slug:slug>/update/",
         views.PostUpdateView.as_view(), name="update-post"),
    path("posts/<slug:slug>/like/",
         views.PostLikeView.as_view(),
         name="like-post"),
    path("pet-care", views.care_tips, name="pet-care-page"),
    path("our-mission", views.our_mission, name="our-mission-page")
]
