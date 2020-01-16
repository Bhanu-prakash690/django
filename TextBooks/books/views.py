from django.shortcuts import render
from .models import Book

# Create your views here.
def home(request):
    return render(request, 'books/index.html')

def books_(request, tag):
    try:
        books__ = Book.objects.filter(category=tag)
    except:
        books__ = []

    context = {
        'books':books__
    }

    return render(request, 'books/books.html', context)
