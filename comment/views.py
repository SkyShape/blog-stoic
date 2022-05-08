from django.views.generic import ListView
from django.shortcuts import render

from comment.models import Comment

class CommentListView(ListView):
    template_name = 'comment/create-comment.html'
    model = Comment

    