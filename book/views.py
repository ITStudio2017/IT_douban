from django.shortcuts import render
from .models import Book, Label, get_alllabel
from .forms import BookFrom
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
    back = {
        'message': "",
        'form': None,
    }

    form = None
    if request.method == 'GET':
        form = BookFrom()
    if request.method == 'POST':
        form = BookFrom(request.POST, request.FILES)
        if form.is_valid():
            bookname = form.cleaned_data['bookname']
            introduction = form.cleaned_data['introduction']
            author = form.cleaned_data['author']
            label = 101
            cover = form.cleaned_data['cover']
            newBook = Book(bookname=bookname, introduction=introduction, author=author, label=label, cover=cover, owner=1)
            newBook.save()
        else:
            back['message'] = u"错误"

    back['form'] = form
    return render(request, 'book_edit.html', back)


def book_change(request):
    return


def book_delete(request):
    return
