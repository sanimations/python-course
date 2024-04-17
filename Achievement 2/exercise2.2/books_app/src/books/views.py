from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists
from .models import Book                #to access Book model

class BookListView(ListView):            #class-based view
    model = Book                         #specify model
    template_name = 'books/main.html'    #specify template 

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail.html'
