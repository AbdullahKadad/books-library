from django.contrib import admin
from django.urls import path
from .views import  *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('books', Books.as_view(), name='books'),
    path('bookdetails/<int:pk>', BookDetails.as_view(), name='bookdetails'),
]
