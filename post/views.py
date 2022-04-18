from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

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
