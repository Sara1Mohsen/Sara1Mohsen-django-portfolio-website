from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


from .filters import PostFilter

# Create your views here.
def home(request):
    Posts = Post.objects.filter(active=True  , featured=True)[:3]

    context = {'posts': Posts}
    return HttpResponse(render(request, 'base/index.html', context))

def POSTS(request):
    posts = Post.objects.filter(active=True)
    myfilter = PostFilter(request.GET, queryset=posts)
    posts = myfilter.qs
    page = request.GET.get('page')
    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
    except EmptyPage:
        page = paginator.num_pages 
    
    context = {'posts': posts ,'myfilter': myfilter}

    return HttpResponse(render(request, 'base/posts.html', {'posts': posts}))

def POST(request , pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return HttpResponse(render(request ,'base/post.html',  context))

def Profile(request):
    posts = Post.objects.filter(active=True)
    return render(request, 'base/profile.html', {'posts': posts})

def main(request):
    return render(request ,'base/main.html')

@login_required(login_url='home')
def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()

        return redirect('posts')

    context = {'form': form}
    return render(request ,'base/post_form.html', context)

@login_required(login_url='home')
def update_post(request ,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES , instance=post)
        if form.is_valid():
            form.save()

        return redirect('posts')

    context = {'form': form}
    return render(request ,'base/post_form.html', context)

@login_required(login_url='home')
def delete_post(request ,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    context = {'item': post}
    return render(request ,'base/delete.html', context)

def send_email(request):
    if request.method == 'POST':
        template = render_to_string('base/email_template.html',{
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'message': request.POST.get('message'),
        })
        email = EmailMessage(
            request.POST.get('subject'),
            template,
            settings.EMAIL_HOST_USER,
            ['saramohsen0901@gmail.com']
        )
        email.fail_silently = False
        email.send()
    return render(request ,'base/email_sent.html', {'some_flag': True})