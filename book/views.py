from django.shortcuts import render
from .models import Book, Label, get_alllabel
import logging


def book_list(request, label: int=None, search: str=""):
    back = {}
    back['labelAll'] = {}
    back['books'] = None
    back['message'] = ""
    back['search'] = ""

    back['search'] = search

    back['labelAll'] = get_alllabel()

    bookSet = Book.objects
    if label:
        if label in range(1, 100):
            label = label*100
            bookSet = bookSet.filter(label__range=(label, label + 100))
        else:
            bookSet = bookSet.filter(label=label)
    if search:
        bookSet = bookSet.filter(bookname__contains=search)
    bookSet = bookSet.order_by("lastEditTime")
    back['books'] = bookSet

    if bookSet:
        pass
    else:
        back['message'] = u"没有书籍"

    return render(request, 'book_index.html', back)


def book_new(request):
    back = {}
    if request.method == 'GET':
        return render(request, 'book_edit.html', back)
    if request.method == 'POST':

        return render(request, 'book_edit.html', back)
    return render(request, 'book_edit.html', back)


def book_change(request):
    return


def book_delete(request):
    return
