from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from posts_app.forms import PostForm, CommentForm, CategoryForm
from posts_app.models import Post, Comment, Category


# Create your views here.

def show_posts(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts
    }
    return render(request, 'posts_app/home.html', context=ctx)

def show_category(request):
    categories = Category.objects.all()
    ctx = {
        'categories': categories
    }
    return render(request, 'posts_app/category.html', context=ctx)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    ctx = {
        'form': form
    }
    return render(request, 'posts_app/add_post.html',context=ctx)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryForm()
    ctx = {
        'form': form
    }
    return render(request, 'posts_app/add_category.html', context=ctx)


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_info', pk=post.pk)
    else:
        form = PostForm(instance=post)
    ctx = {
        'form': form,
        'post': post,
    }
    return render(request, 'posts_app/edit_post.html', context=ctx)

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    ctx = {'post': post}
    return render(request, 'posts_app/delete_post.html', context=ctx)
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category')
    ctx = {'category': category}
    return render(request, 'posts_app/delete_category.html', context=ctx)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryForm(instance=category)
    ctx = {
        'form': form,
        'category': category,
    }
    return render(request, 'posts_app/edit_category.html', context=ctx)
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_info', pk=pk)
    else:
        form = CommentForm()
    ctx = {
        'form':form
    }
    return render(request, 'posts_app/add_comment.html', context=ctx)

def post_info(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    ctx = {
        'post': post,
        'comments': comments
    }
    return render(request, 'posts_app/post_info.html', context=ctx)

def category_info(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category)
    ctx = {
        'category': category,
        'posts': posts
    }
    return render(request, 'posts_app/category_info.html', context=ctx)


def create_posts(request):
    user = User.objects.first()
    category = Category.objects.first()

    if not user or not category:
        return HttpResponse("Ошибка")

    for i in range(10):
        Post.objects.create(
            title=f' {i+1}',
            content=f' {i+1}.',
            author=user,
            category=category
        )

    return HttpResponse("добавлено 10 записей")

def update_post_titles(request):
    posts = Post.objects.all()
    for post in posts:
        post.title = f'{post.title} ({post.id})'
        post.save()

    return HttpResponse("Успешно обновлено")

def delete_id_posts(request):
    posts = Post.objects.all()
    for post in posts:
        if post.id % 2 != 0:
            post.delete()

    return HttpResponse("Успешно удалено")