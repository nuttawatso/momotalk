from django.shortcuts import render
from .forms import PostsForm
import datetime
from .models import Posts
import requests
from django.contrib import messages


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
        url = "https://api.aiforthai.in.th/ssense"
        text = form.instance
        
        data = {'text':text}
        
        headers = {
            'Apikey': "vM0LY7YAGqM2DhFbJHI3ON5mmg71vs9K"
            }
        
        response = requests.post(url, data=data, headers=headers)
        result = (response.json()['sentiment']['polarity'])
        if (result == 'negative' ):
            print('กรุณาพิมพ์ให้สุภาพ')
            messages.warning(request,'กรุณาพิมพ์ให้สุภาพหรือตามกฏ')            
        else:
            print('บันทึกสำเร็จ')
            print(response.json())
            form.save()
            messages.success(request,'โพสต์สำเร็จ')   
             
    context['form']= form
    return render(request, "createpost.html", context)

    



def read_post_all(request):
  posts = Posts.objects.all()
  stringval=""
  for post in  posts:
      stringval += post.description + post.title
  return render(request,stringval) 