from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Followers, User
user = get_user_model()


class User_login(View):
    
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else: 
         messages.error(request, "password or username error.")
         return render(request, 'login.html')
     
     
class SignUp(View):
    def get(self, request):
      return render(request, 'login.html')
  
  
    def post(self, request):
        first_name = request.POST.get('first_name')  
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeatPassword = request.POST.get('repeatPassword')     
        
        if password == repeatPassword:
            try:
                user.objects.create(
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    username = username,
                    password = make_password(password)
                )
            except Exception as e:
                print(e )
            newUser = authenticate(username=username, password=password)
            if newUser is not None:
                login(request, newUser)
                return redirect('home_page')
            else: 
                messages.error(request, "error in data.")
                return render(request, 'login.html')
        
        return redirect('home_page')

def user_logout(request):
    logout(request)
    
    return redirect('user_login')     

def profile(request):
    return render(request, 'profile.html')

def public_profile(request, pk):
    profile = user.objects.get(id=pk) 
    is_following = Followers.objects.filter(user=request.user, kuzataman=profile).exists()
    context = {
        'profile': profile,
        'is_following': is_following
    }
    return render(request, 'public_profile.html', context)




def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    Followers.objects.get_or_create(user=request.user, kuzataman=user_to_follow)
    return redirect('public_profile', pk=user_id)

def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    Followers.objects.filter(user=request.user, kuzataman=user_to_unfollow).delete()
    return redirect('public_profile', pk=user_id)

