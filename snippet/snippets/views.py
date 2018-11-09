from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Snippet
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Product, Post
from .filters import SnippetFilter, ProductFilter, PostFilter


class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/snippet_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SnippetFilter(self.request.GET, queryset=self.get_queryset())
        return context


class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippets/snippet_detail.html'


def product_list(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'products/product_list.html', {'filter': f})


def post_list(request):
    f = PostFilter(request.GET, queryset=Post.objects.all())
    return render(request, 'products/post_list.html', {'filter': f})