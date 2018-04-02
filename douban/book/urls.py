from django.conf.urls import url
from .views import book_list, book_new, book_change, book_delete, book_show

urlpatterns = [
    url(r'^index/l(\d*)/s(.*)/$', book_list, name='book_list'),
    url(r'^newbook/$', book_new, name='book_new'),
    url(r'^showbook/(\d+)/$', book_show, name='book_show'),
    url(r'^changebook/(\d+)/$', book_change, name='book_change'),
]