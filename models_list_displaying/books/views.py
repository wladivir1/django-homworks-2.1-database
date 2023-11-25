from django.shortcuts import render, get_object_or_404
from books.models import Book
from books.converters import DateConverter

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)

def book_view(request, pub_date):
    template = 'books/book.html'
    books = get_object_or_404(Book, pub_date=pub_date)
    book_next = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()    
    book_back = Book.objects.filter(pub_date__lt=pub_date).order_by('pub_date').first()    
    
    context = {
            'book': books,
            'book_next': book_next,
            'book_back': book_back
            }
    
    return render(request, template, context)
