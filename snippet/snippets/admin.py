from django.contrib import admin

from .models import Snippet, Product, Post, Comment

# Register your models here.
admin.site.register(Snippet)
admin.site.register(Product)
admin.site.register(Post)
admin.site.register(Comment)
