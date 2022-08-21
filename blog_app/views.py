from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView, DetailView

from blog_app.models import Post


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class PostDetailView(DetailView):
    model = Post
    template_name = 'details.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'






def home(request):
    return render(request, 'base.html', )


