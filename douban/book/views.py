from django.shortcuts import render
from .models import Book, Label, Comment, get_alllabel, get_label_by_int
from .forms import BookFrom, CommentForm
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
        label = int(label)
        if label in range(1, 100):
            label = label * 100
            bookSet = bookSet.filter(label__range=(label, label + 100))
            logging.debug(label)
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


def book_show(request, bookId: int = None):
    back = {
        'message': "",
        'book': None,
        'fLabel': "",
        'sLabel': "",
        'comments': None,
    }
    try:
        book = Book.objects.get(id=bookId)
        back['book'] = book
        try:
            label = book.label
            (fLabel, sLabel) = get_label_by_int(label)
            back['fLabel'] = fLabel
            back['sLabel'] = sLabel
        except:
            back['message'] = u"标签错误"
    except:
        back['message'] = u"没有找到这本书"
        return render(request, 'book_show.html', back)

    try:
        comments = Comment.objects.filter(book_id__exact=bookId)
        back['comments'] = comments
    except:
        back['message'] = u"评论加载错误"

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            newComment = Comment(book=book, content=content, owner=1)
            newComment.save()
    else:
        form = CommentForm()
    back['form'] = form
    return render(request, 'book_show.html', back)


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


def book_change(request, bookId: int = None):
    back = {
        'message': "",
        'form': None,
    }

    try:
        book = Book.objects.get(id=bookId)
    except:
        back['message'] = u"没有找到这本书"
        return render(request, 'book_edit.html', back)
    form = None
    if request.method == 'GET':
        data = {
            'bookname': book.bookname,
            'introduction': book.introduction,
            'author': book.author,
            'label': 101,
            'cover': book.cover,
        }
        form = BookFrom(data=data)
    if request.method == 'POST':
        form = BookFrom(request.POST, request.FILES)
        if form.is_valid():
            bookname = form.cleaned_data['bookname']
            introduction = form.cleaned_data['introduction']
            author = form.cleaned_data['author']
            label = 101
            cover = form.cleaned_data['cover']
            book.bookname = bookname
            book.introduction = introduction
            book.author = author
            book.label = label
            book.cover = cover
            book.save()
        else:
            back['message'] = u"错误"

    back['form'] = form
    return render(request, 'book_edit.html', back)


def book_delete(request):
    return
