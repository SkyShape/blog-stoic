from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from post.forms import PostForm
from post.models import Post


class PostCreateView(CreateView):
    template_name = 'post/create-post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('show_all_posts')


class AllPostListView(ListView):
    paginate_by = 3
    template_name = 'post/show-all-post.html'
    model = Post
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.filter(active=True)


class ArchivePostListView(ListView):
    paginate_by = 3
    template_name = 'post/show-arhive-pos.html'
    model = Post
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.filter(active=False)


class PostDetailsView(DetailView):
    template_name = 'post/details-post.html'
    model = Post


def update_like(request, pk):
    obj = Post.objects.get(id=pk)
    like = getattr(obj, 'like_count')
    id_obj = getattr(obj, 'id')
    Post.objects.filter(id=pk).update(like_count=like + 1)
    return redirect('details_post', id_obj)


def update_dislike(request, pk):
    obj = Post.objects.get(id=pk)
    dislike = getattr(obj, 'dislike_count')
    id_obj = getattr(obj, 'id')
    Post.objects.filter(id=pk).update(dislike_count=dislike + 1)
    return redirect('details_post', id_obj)


def archive_post(request, pk):
    Post.objects.filter(id=pk).update(active=False)
    return redirect('show_all_posts')


def undo_archive_post(request, pk):
    Post.objects.filter(id=pk).update(active=True)
    return redirect('show_all_posts')
