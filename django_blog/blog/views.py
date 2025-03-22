from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib import messages


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all().order_by('-created_at')
    form = CommentForm
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'forms': form})
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()(commit = False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post_id)
        else:
            form = CommentForm()
            return render(request, 'blog/add_comment.html', {'form': form, 'post':post})
        
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.author != request.user:
        return HttpResponseForbidden("You do not have permission to edit this comment.")
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.author != request.user:
        return HttpResponseForbidden("You do not have permission to delete this comment.")
    post_id = comment.post.id
    comment.delete()
    return redirect('post_detail', post_id=post_id)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    form_class = PostForm
    template_name = 'blog/confirm_delete.html'
    success_url = reverse_lazy('post-list')
    
    def test_func(self):
        post = self.get.object()
        return self.request.user == post.author
    


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = CustomUserCreationForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})