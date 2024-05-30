from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Post, Like

@login_required
def home(request):
    return render(request, 'post.html')


def getPost(request, pk):
     post = Post.objects.get(pk=pk)

def single_post(request, pk):
    post = getPost(pk=pk)
    
    return render(request, 'single.html', {'post': post})


def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    
    Like.objects.create(
        post=post,
        user=user
    )
    
    return redirect('home_page')

class CreatePost(View):
    def get(self, request):
        post = Post.objects.last()
        
        return render(request, 'my-post.html', {'post': post})
        
    def post(self, request):
        name = request.POST.get('name')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        try:
            post = Post.objects.create(
                author = request.user,
                image = image,
                name = name,
                content = content
            )
        except Exception as e:
            print(e)
            
        return redirect('create_post')    