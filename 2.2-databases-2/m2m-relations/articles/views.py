from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {
        'object_list': Article.objects.order_by('-published_at').prefetch_related('scopes')
    }

    return render(request, template, context)
