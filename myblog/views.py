from django.shortcuts import render,get_object_or_404
from . models import *

# Create your views here.
def index(request):
    articles = Article.objects.all()
    categoryes = Category.objects.all()
    return render(request,'blogg/index.html',{'articles': articles, 'categoryes': categoryes})

def details(request,id):
    post_details = Article.objects.get(id=id)
    categoryes = Category.objects.all()
    return render(request,'blogg/blog-post.html',{'post_details': post_details,'categoryes': categoryes})
    
def category_detail(request,category_id):
    category = get_object_or_404(Category,id=category_id)
    article = Article.objects.filter(category=category)
    categoryes = Category.objects.all()
    return render(request,'blogg/category.html',{'category': category,'articles': article,'categoryes': categoryes})

def about_me(request):
    articles = Article.objects.all()
    categoryes = Category.objects.all()
    return render(request,'blogg/about_me.html',{'articles': articles, 'categoryes': categoryes})
