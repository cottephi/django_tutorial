from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect


def blog_list(request):
    # noinspection PyUnresolvedReferences
    post = Post.objects.all()
    context = {"blog_list": post}
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, post_id):
    # noinspection PyUnresolvedReferences
    each_post = Post.objects.get(id=post_id)
    context = {"blog_detail": each_post}
    return render(request, "blog/blog_detail.html", context)


def blog_delete(request, post_id):
    # noinspection PyUnresolvedReferences
    each_post = Post.objects.get(id=post_id)
    each_post.delete()
    return HttpResponseRedirect("/")
