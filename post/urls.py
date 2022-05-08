from django.urls import path

from post import views

urlpatterns = [
    path('create-post/', views.PostCreateView.as_view(), name='create_post'),
    path('update-post/<int:pk>/', views.PostUpdateView.as_view(), name='update_post'),
    path('show-all-posts/', views.AllPostListView.as_view(), name='show_all_posts'),
    path('archive-post/<int:pk>/', views.archive_post, name='archive_post'),
    path('undo-archive-post/<int:pk>/', views.undo_archive_post, name='undo_archive_post'),
    path('show-archive-posts/', views.ArchivePostListView.as_view(), name='show_archive_posts'),
    path('details-post/<int:pk>/', views.PostDetailsView.as_view(), name='details_post'),
    path('update-like-post/<int:pk>/', views.update_like, name='update_like_post'),
    path('update-dislike-post/<int:pk>/', views.update_dislike, name='update_dislike_post'),
    path('all-topics/', views.all_topics, name='topic'),
]
