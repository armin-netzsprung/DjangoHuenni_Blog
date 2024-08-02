
from django.db import models
from django.conf import settings
from django.utils import timezone

from tinymce import models as tinymce_models
from django.contrib.auth.models import User


class Category1(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories1"
    
    def __str__(self):
        return self.name    

class Category2(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories2"
    
    def __str__(self):
        return self.name    

class Category3(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories3"
    
    def __str__(self):
        return self.name    

class Category4(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories4"
    
    def __str__(self):
        return self.name    

class Category5(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories5"
    
    def __str__(self):
        return self.name    


class TypOfBlogPage(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name    

class RubricSpruch(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name    

class Rubric(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name    

class Post(models.Model):
    TypOfBlogPage = models.ManyToManyField("TypOfBlogPage", related_name="posts")
    rubric = models.ManyToManyField("Rubric", related_name="posts")
    title = models.CharField(max_length=200)
    category1 = models.ManyToManyField("Category1", related_name="posts")
    category2 = models.ManyToManyField("Category2", related_name="posts")
    category3 = models.ManyToManyField("Category3", related_name="posts", blank=True )
    category4 = models.ManyToManyField("Category4", related_name="posts", blank=True )
    category5 = models.ManyToManyField("Category5", related_name="posts", blank=True )
    content = tinymce_models.HTMLField(default="", null=True, blank=True )
    contentshort = tinymce_models.HTMLField(default="", null=True, blank=True )
    banner_bild = models.ImageField(upload_to ='huenni_blog', default='huenni_blog/default.jpg') 
    content_attachment = models.FileField(upload_to ='huenni_blog', default='huenni_blog/default.jpg') 

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True )
    published_date = models.DateTimeField(auto_now=True )
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title    
    

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    comment = tinymce_models.HTMLField(default="")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True )
    published_date = models.DateTimeField(auto_now=True )

    def __str__(self):
        return f"{self.author} on '{self.comment}'"

# ### AH
# Sprüche
# ###

class Spruch(models.Model):
    rubricspruch = models.ManyToManyField("RubricSpruch", related_name="posts")
    erfinder = models.CharField(max_length=200)
    content = tinymce_models.HTMLField(default="", null=True, blank=True )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True )
    published_date = models.DateTimeField(auto_now=True )
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.erfinder





