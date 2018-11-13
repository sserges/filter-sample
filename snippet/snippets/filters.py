import django_filters

from .models import Snippet, Product, Post, Comment

class SnippetFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )

    updated__date = django_filters.DateFilter(label='Updated date')

    # ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

    # order = django_filters.OrderingFilter(
    #     label='Ordering 2',
    #     fields=(
    #         ('created', 'created')
    #     )
    # )

    class Meta:
        model = Snippet
        fields = [
            # 'title': ['icontains'],
            # 'body': ['icontains']
            # 'updated'
        ]

    def filter_by_order(self, queryset, name, value):
        expression = 'created' if value == 'ascending' else '-created'
        return queryset.order_by(expression)


class ProductFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='icontains')

    # price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    # release_year = django_filters.NumberFilter(field_name='release_date', lookup_expr='year')
    # release_year__gt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__gt')
    # release_year__lt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__lt')


    class Meta:
        model = Product
        fields = {
            # 'price': ['lte', 'gt'],
            # 'release_date': ['exact', 'year__gt'],
        }


class PostFilter(django_filters.FilterSet):

    # comment = django_filters.CharFilter(label='Comment', method='filter_by_comment')
    # comment__content = django_filters.CharFilter(label='Comment content', lookup_expr='icontains')
    comment__content = django_filters.CharFilter(label='Comment content')

    class Meta:
        model = Post
        fields = [
            'title',
        ]

    # def filter_by_comment(self, queryset, name, value):
    #     return queryset.filter(comment__content__icontains=value).distinct()
