# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import BlogPostForm
from django.shortcuts import redirect

def post_detail(request, db_id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'blogpostdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    post = get_object_or_404(Post, pk=db_id)  # pk is primary key
    post.views += 1  # clock up the number of post views
    post.save()
    staff = request.user.is_staff
    return render(request, "blog/blogpostdetail.html", {'post': post,
                                                   'staff': staff})


def post_list(request):
    """
    Create a view that will return a 
    list of Posts that were published prior to 'now'
    and render them to the 'post_your_blog.html' template
    """
    posts = get_object_or_404(date_published_lte = timezone.now()
        ).order_by('date')
    return render(request, "templates/blog/post_your_blog.html", {'post': post,
    	                                                          'staff': staff,})

def post_details(request, id):
    post = get_object_or_404(Post, pk=db_id) #pk is primary key
    post.views += 1 #clock up the number of post views
    post.save()
    staff = request.user.is_staff
    return render(request, "templates/blog/blogpostdetail.html", {'post': post,
                                                                  'staff': staff}) 

def new_post(request):
    if request.method == "POST":
        form =BlogPostForm(request.POST, request.INFO)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_published = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'templates/blog/blogform.html',{'form': form})

