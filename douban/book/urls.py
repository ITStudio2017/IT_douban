from django.conf.urls import url
from .views import book_list, book_new, book_change, book_delete, book_show


urlpatterns = [
    url(r'^index/$', book_list, name='book_list'),
    url(r'^showbook/(\d+)/$', book_show, name='book_contain'),
    url(r'^booklist/$', book_list, name='book_list'),
    # url(r'^get_label/(?P<obj_id>\d+)', twice_label_choice),
]