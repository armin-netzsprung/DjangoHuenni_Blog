
from django.contrib import admin
from huenni_blog.models import *


class PostAdmin(admin.ModelAdmin):
    pass

class RubricAdmin(admin.ModelAdmin):
    pass

class Category1Admin(admin.ModelAdmin):
    pass
class Category2Admin(admin.ModelAdmin):
    pass
class Category3Admin(admin.ModelAdmin):
    pass
class Category4Admin(admin.ModelAdmin):
    pass
class Category5Admin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class TypOfBlogPageAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

class SpruchAdmin(admin.ModelAdmin):
    pass

class RubricSpruchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Rubric, RubricAdmin)

admin.site.register(Category1, Category1Admin)
admin.site.register(Category2, Category2Admin)
admin.site.register(Category3, Category3Admin)
admin.site.register(Category4, Category4Admin)
admin.site.register(Category5, Category5Admin)

admin.site.register(Post, PostAdmin)
admin.site.register(TypOfBlogPage, PostAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.register(Spruch, SpruchAdmin)
admin.site.register(RubricSpruch, RubricSpruchAdmin)
