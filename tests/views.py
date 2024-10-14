from django.shortcuts import render
from rest_framework.views import APIView
from . import serializers as ser
from . import models as md
from rest_framework.response import Response 
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class BookList(APIView):
    def get(self, request, format=None):
        books = md.Book.objects.all()
        serializer = ser.BookListSerializers(books, many=True)
        return Response(serializer.data)
    

class BookDetail(APIView):
    def get(self, request, pk):
        book = md.Book.objects.get(id=pk)
        serializer = ser.BookDetailSerializers(book)
        return Response(serializer.data)



class BookSearch(generics.ListAPIView):
    serializer_class = ser.BookListSerializers
    queryset = md.Book.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['category', 'author', 'is_published', 'publication_date']
    search_fields = ['title', 'author']         