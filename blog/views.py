from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.published.all()
    context = {'posts': posts}
    template_name = 'blog/post/list.html'
    return render(request, template_name, context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    context = {'post': post}
    template_name = 'blog/post/detail.html'
    return render(request,  template_name, context)