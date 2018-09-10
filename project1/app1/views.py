from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import BasicForm
from .models import Blog
from .serializers import BlogPostSerializer
from django.core import serializers
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')
def home(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            form.save()
            objects = Blog.objects.all()
            if request.user.is_authenticated():
                c_user = request.user
                data = serializers.serialize("json", Blog.objects.filter(user=c_user.pk).all())
                return HttpResponse(data, content_type="application/json")


    form = BasicForm()
    context = {'form':form}
    return render(request,'base.html',context)
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'{% %}')
        else:
            return redirect('register.html')
    else:
        form = UserCreationForm()
        context= {'form':form}
        return render(request,'register.html',context)


def user(request):
    serializer_class = BlogPostSerializer()
    c_user = request.user

    data = serializers.serialize("json", Blog.objects.filter(user=c_user.pk).all())



    return HttpResponse(data, content_type="application/json")
