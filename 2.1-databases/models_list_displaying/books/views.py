from django.shortcuts import render
from django.utils.text import slugify
from books.models import Book
# from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    context = {
        'books': Book.objects.all()
    }
    return render(request, template, context)


def one_book(request, slug):
    template = 'books/one_book.html'
    books = []
    for book in Book.objects.all():
        books.append(book.slug)
    books = sorted(books)
    index = books.index(slug)
    last_index = len(books) - 1
    context = {
        'book': Book.objects.get(slug=slug),
        'books': books,
        'index': index,
        'last_index': last_index,
        'prev_book': books[index-1]
        
    }
    if index < len(books) - 1:
        context['next_book'] = books[index+1]
    return render(request, template, context)

    # page_number = pages.index(slug)+1
    # paginator = Paginator(sorted(pages), len(pages))
    # page = paginator.get_page(page_number)

