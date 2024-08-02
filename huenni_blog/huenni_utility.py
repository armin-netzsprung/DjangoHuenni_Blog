from .models import *

def blog_cats1(request):
    # posts = Post.objects.filter(TypOfBlogPage='Blog').order_by('-published_date')
    cats1 = Category1.objects.order_by('name')
    return {'cats1': cats1}

def blog_posts(request):
    posts = Post.objects.order_by('-published_date')
    return {'blog_posts': posts}

def blog_rubric(request):
    rubric = Rubric.objects.order_by('name')
    return {'blog_rubric': rubric}
    
def spruch_post(request):
    spruchposts = Spruch.objects.order_by('-published_date')
    return {'spruch_posts': spruchposts}
    

