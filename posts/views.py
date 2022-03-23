from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import PostsForm
from django.contrib import messages


# Create your views here.
def index(request):
    form = PostsForm()
    data = Post.objects.all()
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Contact saved successfully.')
            return redirect('index')
    return render(request, 'index.html', {'title': 'Add New Post', 'form': form, 'rows': data})
