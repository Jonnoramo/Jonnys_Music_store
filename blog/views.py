from django.shortcuts import render
from django.utils import timezone
from .models import PostBlog
from django.shortcuts import render, get_object_or_404
from .forms import BlogPostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def post_list(request):
    """
    Create a view that will return a
    list of Posts that were published prior to'now'
    and render them to the 'blog_posts.html' template
    """
    posts = PostBlog.objects.filter(published_date__lte = timezone.now()
        ).order_by('-published_date')
    return render(request, "blog/blog_posts.html", {'posts': posts})

@login_required
def post_details(request, id):
    post = get_object_or_404(PostBlog, pk=id)
    post.views += 1
    post.save()
    return render(request, "blog/blog_post_detail.html", {'post': post})

@login_required
def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_details, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_post_form.html', {'form': form})

def _get_failure_view():
    """
    Returns the view to be used for CSRF rejections
    """
    return get_callable(settings.CSRF_FAILURE_VIEW) 