from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from post.forms import PostForm
from post.models import Post, Topic


class PostCreateView(CreateView):
    template_name = 'post/create-post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('show_all_posts')


class PostUpdateView(UpdateView):
    template_name = 'post/create-post.html'
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('show_all_posts')


class AllPostListView(ListView):
    model = Post
    template_name = 'post/show-all-post.html'
    context_object_name = 'all_posts'
    queryset = Post.objects.filter(active=True)
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_topics'] = Topic.objects.all()
        return context


class ArchivePostListView(ListView):
    paginate_by = 4
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
