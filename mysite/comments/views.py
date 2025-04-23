from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Comment

@login_required
def comment_list(request):
    comments = Comment.objects.all().order_by('-created_at')
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect("comments:comment_list")
    return render(request, "comments/comment_list.html", {"form": form, "comments": comments})
