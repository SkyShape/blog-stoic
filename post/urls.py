from django.urls import path

from post import views

urlpatterns = [
    path('create-post', views.PostCreateView.as_view(), name='create_post'),
    path('show-all-posts', views.AllPostListView.as_view(), name='show_all_posts')
]
