from django.shortcuts import render
from .forms import PostsForm
import datetime
from .models import Posts


# Create your views here.
def home(request):
    posts = Posts.objects.all()
    return render(request,'home.html', {"posts":posts})

# def createpost(request):
#     return render(request,'createpost.html',)

def consult(request):
    posts = Posts.objects.all()
    return render(request,'consult.html',{"posts":posts})
def general(request):
    posts = Posts.objects.all()
    return render(request,'general.html',{"posts":posts})
def learning(request):
    posts = Posts.objects.all()
    print(posts)
    return render(request,'learning.html',{"posts":posts})
def love(request):
    posts = Posts.objects.all()
    return render(request,'love.html',{"posts":posts})




def createpost(request):
    context ={} 
    form = PostsForm(request.POST or None) 
    if form.is_valid():
        print(form.instance)
        
        form.save()          
    context['form']= form
    return render(request, "createpost.html", context)

    



def read_post_all(request):
  posts = Posts.objects.all()
  stringval=""
  for post in  posts:
      stringval += post.description + post.title
  return render(request,stringval) 