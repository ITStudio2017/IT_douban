from django.conf.urls import url
from .views import book_list, book_new, book_change, book_delete

urlpatterns = [
    url(r'^index/l(\d*)/s(.*)/$', book_list, name='list'),
]