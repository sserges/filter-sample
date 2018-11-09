from django.db import models


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:50]


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.TextField()
    release_date = models.DateField()
    # manufacturer = models.ForeignKey(Manufacturer)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
