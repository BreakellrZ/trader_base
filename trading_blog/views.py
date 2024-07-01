from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Journal



# Create your views here.
class PostList(generic.ListView):
    queryset = Journal.objects.all().order_by("-date")
    template_name = "post.html"
    paginate_by = 3

# Taken code from code institute I think therefore I blog walkthrough
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Journal.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.journal_comments.all().order_by("-created_on")
    comment_count = post.journal_comments.filter(approved=True).count()

    return render(
        request,
        "post_detail.html",
        {
          "post": post,
          "comments": comments,
          "comment_count": comment_count,
          },
    )