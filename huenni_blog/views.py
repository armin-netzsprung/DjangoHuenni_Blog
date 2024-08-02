
from django.utils import timezone


import json
from django.http import HttpRequest                 # beinhaltet die Http Request Typen, wie z. B. Post, Get, ...
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render                 # gibt die gerenderten Daten z. B. zur Ansicht in einer HTML Seite

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from huenni_blog.forms import PostFormular                 # Stellt Informationen schöner dar und enthält vordefinierte Templates, wie z. B. für Wichtig, Info, usw. zur Verfügung
from .models import *

from django.core.paginator import Paginator, EmptyPage     # Bibliothek für die Pagnitierung der Seiten bei vielen Einträgen

# ############################################################
# Blog
# ###

def post_list(request):
    # ### AH
    # order_by('-published_date'): das Minuszeichen sortiert das jüngste zu erst
    # ###

    # posts = Post.objects.filter(TypOfBlogPage='Blog').order_by('-published_date')
    posts = Post.objects.order_by('-published_date')

    # ### AH
    # Paginator: Damit es nicht zu lange dauert beim Laden der Posts, werden nur eine
    # Anzahl x an Einträgen zurückgegeben und im Template kann man durch die Seiten 
    # klicken
    # ###
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'huenni_blog/post_list.html', {'posts': posts})

# ### AH
# Filtert die Liste aller Blogeinträge, der ausgewählten Kategorie und filtert danach
# order_by('-published_date'): das Minuszeichen sortiert das jüngste zu erst
# ###
def post_list_title(request, filter: str):
    posts = Post.objects.filter(title=filter).order_by('-published_date')

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'huenni_blog/post_list.html', {'posts': posts})

def post_list_rubric(request, filter: str):
    posts = Post.objects.filter(rubric__name=filter).order_by('-published_date')

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'huenni_blog/post_list.html', {'posts': posts})

def post_list_category1(request, filter: str):
    posts = Post.objects.filter(category1=filter).order_by('-published_date')

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'huenni_blog/post_list.html', {'posts': posts})


@login_required(login_url='login')
def post_create(request: HttpRequest):
    if request.method == "POST":
        if 'Speichern' in request.POST:
            form = PostFormular(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Post wurde erfolgreich aktualisiert.")    
        elif 'Abbruch' in request.POST:
                messages.success(request, "Post wurde NICHT aktualisiert.")    
        return redirect("post_list")
    else:
        form = PostFormular()
    ctx = {"form": form}                     
    return render(request, "huenni_blog/post_form.html", ctx)   
    
def post_detail(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.all()
    context = {"post": post, "comments": comments}
    return render(request, "huenni_blog/post_detail.html", context)


@login_required(login_url='login')
def post_update(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # ### AH
        # Wichtig: request.FILES ist notwendig, sonst werden die Bilder nicht upgedated!
        # ###
        form = PostFormular(request.POST, request.FILES, instance=post)
        
        
        if 'Speichern' in request.POST:
            if form.is_valid():
                form.save()
                messages.success(request, "Post wurde erfolgreich aktualisiert.")    
        elif 'Abbruch' in request.POST:
                messages.success(request, "Post wurde NICHT aktualisiert.")    
        return redirect("post_list")
    else:
        form = PostFormular(instance=post)
    context = {"form": form, "post": post}
    return render(request, "huenni_blog/post_form.html", context)


@login_required(login_url='login')
def post_delete(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post wurde erfolgreich gelöscht.")
        return redirect("post_list")
    context = {"post": post}
    return render(request, "huenni_blog/post_confirm_delete.html", context)

@login_required(login_url='login')
def post_comment_delete(request: HttpRequest, pk: int):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        comment.delete()
        messages.success(request, "Kommentar wurde erfolgreich gelöscht.")
        return redirect("post_list")
    context = {"comment": comment}
    return render(request, "huenni_blog/post_comment_confirm_delete.html", context)

# ### AH
# Kommentare
@login_required(login_url='login')

def AddComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)

        comment_instance = Comment(comment=comment, author=user, post=post)
        comment_instance.save()
        messages.success(request, "Der Kommentar wurde erfolgreich hinzugefügt.")
    else:
        messages.error(request, "FEHLER! Kommentar konnte nicht hinzugefügt werde!")

    return redirect(f'post_list')


