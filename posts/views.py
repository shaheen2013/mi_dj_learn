from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import PostsForm, PostSeoInlineFormset
from django.contrib import messages


# Create your views here.
def index(request):
    form = PostsForm()
    post_seo_formset = PostSeoInlineFormset()
    data = Post.objects.all()
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Contact saved successfully.')
            return redirect('index')
    return render(request, 'index.html',
                  {'title': 'Add New Post', 'form': form, 'rows': data, 'post_seo_formset': post_seo_formset})
