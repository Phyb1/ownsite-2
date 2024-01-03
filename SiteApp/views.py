from django.http import request
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from SiteApp.forms import CommentForm, ServicesForm
from .models import Blogs, Projects, Services, Comment

def index(request):
    '''the index page'''
    return render(request, 'SiteApp/index.html')


def blogIndex(request):
    '''serves a sinppet of the last five blog entries with a button to
     load more and to read the blog in detail'''
    data = Blogs.objects.order_by('pubDate')[:5]
    context = {'data':data}
    return render(request, 'SiteApp/blogIndex.html', context)


def blogReader(request, blog_id):
    '''serves the full blog text '''
    data = get_object_or_404(Blogs, id=blog_id)
    comments = Comment.objects.filter(title=blog_id).order_by('-date')
    context = {'data':data, 'comments':comments, 'next':blog_id+1, 'prev':blog_id-1}
    return render(request, 'SiteApp/blog.html', context)


def comment(request, blog_id):
    '''allowing comments from users '''
    data = Blogs.objects.get(id=blog_id)
    if request.method != 'POST':
        form = CommentForm()
        comments =Comment.objects.filter(title=blog_id).order_by('-date')
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():            
            new_form = form.save(commit=False)
            new_form.title = data
            new_form.save()
            comments =Comment.objects.filter(title=blog_id).order_by('-date')
            context = {'data':data, 'comments':comments, 'next':blog_id+1, 'prev':blog_id-1}
            return render(request, 'SiteApp/blog.html', context)
    context = {'data':data, 'comments':comments, 'form':form, 'next':blog_id+1, 'prev':blog_id-1}
    return render(request, 'SiteApp/blog.html', context)


def projects(request):
    '''serving list of current projects'''
    data = Projects.objects.order_by('startDate')
    context = {'data':data}
    return render(request, 'SiteApp/projectIndex.html', context)


def about(request):
    '''serving the about page'''
    return render(request, 'SiteApp/about.html')


def contact(request):
    '''serving the contact page'''
    return render(request, 'SiteApp/contact/html')

def order(request):
     if request.method != 'POST':
        form = ServicesForm()
     else:
        form = ServicesForm(data=request.POST)
        if form.is_valid():            
            new_form = form.save()
            return render(request, 'SiteApp/order.html', context)
     context = {'form':form}
     return render(request, 'SiteApp/blog.html', context)
