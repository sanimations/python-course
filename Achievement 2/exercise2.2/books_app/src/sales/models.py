from django.db import models
from books.models import Book

class Sale(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price =models.FloatField()
    models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.book)