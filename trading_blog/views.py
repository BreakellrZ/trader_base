from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Journal
from .forms import CommentForm




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
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    return render(
        request,
        "post_detail.html",
        {
          "post": post,
          "comments": comments,
          "comment_count": comment_count,
          "comment_form": comment_form,
          },
    )