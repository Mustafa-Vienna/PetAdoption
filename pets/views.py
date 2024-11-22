from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

from .models import Post, Comment
from .forms import CommentForm, UserPostForm
from .topics_data import topics

# Create your views here.


class HomePageView(ListView):
    """
    Ensure to display three latest posts in the homepage
    """
    template_name = "pets/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        """
        Get the latest three posts.
        """
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    """
    Display all posts with pagination
    six posts per page
    """
    template_name = "pets/posts.html"
    model = Post
    paginate_by = 6
    ordering = ["-date"]
    context_object_name = "all_posts"


class SelectedPostView(View):
    """
    Display details of the selected post
    """

    def get(self, request, slug):
        """
        Display the post details, tags, comments and like status
        """
        post = Post.objects.get(slug=slug)
        liked_by_user = post.likes.filter(id=request.user.id).exists()
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "post_like": post.likes.all(),
            "liked_by_user": liked_by_user
        }
        return render(request, "pets/post-detail.html", context)

    def post(self, request, slug):
        """
        Handle comment submission for the selected post
        """
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.email = request.user.email
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment Submitted!'
            )

            return HttpResponseRedirect(reverse(
                "post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "pets/post-detail.html", context)


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Allow create new posts to the authenticated users
    """
    model = Post
    template_name = "pets/create-post.html"
    form_class = UserPostForm
    login_url = 'login'
    success_url = reverse_lazy('posts-page')

    def form_valid(self, form):
        """
        Save the new post and display success msg
        """
        form.instance.author = self.request.user
        messages.success(
            self.request,
            f"The {form.instance.pet_name} post successfully created.")

        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allow authenticated users to delete their own posts
    """
    model = Post
    template_name = "pets/delete-post.html"
    success_url = reverse_lazy("posts-page")
    slug_url_kwarg = 'slug'

    def test_func(self):
        """
        Validate if the current user is the author of the post
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allow authenticated users to update their own posts
    """
    model = Post
    template_name = "pets/create-post.html"
    form_class = UserPostForm
    login_url = 'login'

    def form_valid(self, form):
        """
        Save the updated post and display success msg
        """
        form.instance.author = self.request.user
        self.success_url = reverse('post-detail-page', kwargs={
            'slug': form.instance.slug
        })
        messages.success(
            self.request,
            f"The {form.instance.pet_name} post successfully updated")

        return super().form_valid(form)

    def test_func(self):
        """
        Check if the current user is the author of the post
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostLikeView(View):
    """
    Handle liking and unliking posts
    """
    def post(self, request, slug):
        """
        Toggle like status for a post
        """
        post = Post.objects.get(slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.error(request, "You have just unliked this post.")

        else:
            post.likes.add(request.user)
            messages.success(request, "You just liked this post.")

        return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))


def handler404(request, exception):
    """
    Render the custom 404 error page
    """
    return render(request, '404.html', status=404)


def care_tips(request):
    """
    Render the pet care tips page with topics data
    """
    return render(request, 'pets/includes/pet-care.html', {'topics': topics})


def our_mission(request):
    """
    Render the organization mission page
    """
    return render(request, 'pets/includes/our-mission.html')
