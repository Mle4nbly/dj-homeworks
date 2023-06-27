import json

from django.utils.text import slugify
from django.core.management.base import BaseCommand
from books.models import Book



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('fixtures/books.json', 'r', encoding='utf8') as f:
            books = json.load(f)

        for book in books:
            Book.objects.create(
                name = book['fields']['name'],
                author = book['fields']['author'],
                pub_date = book['fields']['pub_date'],
                slug = slugify(book['fields']['pub_date']),
            )
            