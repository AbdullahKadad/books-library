from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class Books(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_books'] = self.get_queryset().count()  # Calculate total number of books
        return context


class BookDetails(DetailView):
    model = Book
    template_name = 'bookDetails.html'