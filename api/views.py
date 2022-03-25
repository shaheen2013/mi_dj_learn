from django.core.serializers import serialize
from posts.models import Post
from django.http import HttpResponse


# Create your views here.
def posts(request, pk=None):
    if pk is None:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(pk=pk)

    posts = serialize('json', posts, fields=('title', 'image', 'content', 'created_at', 'user', 'category'),
                      use_natural_foreign_keys=True)
    return HttpResponse(posts, content_type='text/json')
