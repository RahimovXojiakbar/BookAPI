from django.urls import path
from . import views as vw
urlpatterns = [
    path('books/', vw.BookList.as_view(), name='book_list_url'),
    path('detail/<int:pk>/', vw.BookDetail.as_view(), name='book_detail_url'),
    path('search/', vw.BookSearch.as_view(), name='book_search_url'),
]