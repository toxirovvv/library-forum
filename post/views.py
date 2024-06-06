from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Post, Like, Comment

@login_required
def home(request):
    return render(request, 'post.html')
   
def getPost(pk):
    post = Post.objects.get(pk=pk)
    return post
def single_post(request, pk):
    post = Post.objects.get(pk=pk)
    
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
    
# def my_likes(request, pk):

# def comment(request):
#     post_id = request.POST.get('id')
    
#     getcontent = request.POST.get('content')
    
#     post = getPost(post_id)
    
#     try:
#         Comment.objects.create(
#             user = request.user,
#             post=post,
#             content=getcontent
#         )
#     except Exception as e:
#         print(e)

#     return redirect('single', post_id)

def comment(request):
    post_id = request.POST.get('id')
    
    getcontent = request.POST.get('content')
    
    post = getPost(post_id)
    
    try:
        Comment.objects.create(
            user=request.user,
            post=post,
            content=getcontent
        )
    except Exception as e:
        print(e)

    return redirect('single', post_id)

def search(request):
    q = request.POST.get('query')
    result = Post.objects.filter(name__icontains=q)
    
    context = {
        'result': result
    }
    
    return render(request, "search.html", context)


@login_required
def my_likes(request):
    likes = Like.objects.filter(user=request.user).select_related('post')
    return render(request, 'my_likes.html', {'likes': likes})

