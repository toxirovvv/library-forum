from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from post.models import Post

# Create your views here.

@login_required
def home_page(request):
    import random

    items = list(Post.objects.all())

    
    random_posts = random.sample(items, 5)
    
    
    return render(request, 'index.html', {'posts': random_posts})