from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists
from .models import Book                #to access Book model
from django.contrib.auth.mixins import LoginRequiredMixin   #to protect class-based view

class BookListView(LoginRequiredMixin, ListView):            #class-based view
    model = Book                         #specify model
    template_name = 'books/main.html'    #specify template 

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/detail.html'
