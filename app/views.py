from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import BlogForm, HashtagForm
from .models import Blog, Hashtag

# Create your views here.
def layout(request):
    return render(request, 'app/layout.html')

def index(request):
    blogs = Blog.objects
    hashtags = Hashtag.objects
    return render(request, 'app/index.html', {'blogs': blogs, 'hashtags': hashtags})

def search(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    return render(request, 'app/search.html', {'hashtag': hashtag})

def new(request):
    return render(request, 'app/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/app/index/')

def blogform(request, blog=None):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.datetime.now()
            blog.save()
            form.save_m2m()
            return redirect('index')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'app/new.html', {'form': form})

def hashtagform(request, hashtag=None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, request.FILES,instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다."
                return render(request, 'app/hashtag.html', {'form': form, "error_message": error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
                return redirect('index')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'app/hashtag.html', {'form': form})

def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return blogform(request, blog)

def remove(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('index')

def detail(request, blog_id):
        blog_detail = get_object_or_404(Blog, pk=blog_id)
        return render(request, 'app/detail.html', {'blog': blog_detail})