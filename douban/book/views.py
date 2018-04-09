from django.core.serializers import json
from django.shortcuts import render, HttpResponse
from .models import Book, FLabel, SLabel, Comment, Praise
from django.core.paginator import Paginator
from .forms import BookFrom, CommentForm
import json
import logging


def dividePage(reqGetList, input):
    back = {}
    back['pass'] = False
    try:
        p = Paginator(input, 4)
        back['pageCount'] = p.num_pages
        index = int(reqGetList['page'])
        back['output'] = p.page(index).object_list
        back['pass'] = True
        back['index'] = index
    except:
        back['pass'] = False
    return back


def book_list(request):
    back = {
        "bookList": {}
    }
    allBook = Book.objects.all().order_by('-score')
    i = 0
    bookList = {}
    for book in allBook:
        i = i + 1
        bookList[str(i)] = {
            "id": book.id,
            "bookname": book.bookname,
            "introduction": book.introduction,
            "author": book.author,
            "cover": book.cover.url,
            "press": book.press,
            "score": book.score,
        }
    back["bookList"] = bookList
    return render(request, "book_list.html", back)


def book_show(request, id):
    back = {
        "book": {},
        "comment": {},
        "form": None,
        "message": "",
        "pageCount": 1,
        "nowPage": 0,
    }

    try:
        getBook = Book.objects.get(id=id)
        star = {
            "1": Comment.objects.filter(score=1).count(),
            "2": Comment.objects.filter(score=2).count(),
            "3": Comment.objects.filter(score=3).count(),
            "4": Comment.objects.filter(score=4).count(),
            "5": Comment.objects.filter(score=5).count(),
        }
        allScoreComment = star["1"] + star["2"] + star["3"] + star["4"] + star["5"]
        score = star["1"] * 1 + star["2"] * 2 + star["3"] * 3 + star["4"] * 4 + star["5"] * 5
        if allScoreComment != 0:
            score = score * 2.0 / allScoreComment
        else:
            score = 5
        score = round(score, 1)
        getBook.score = score
        getBook.save()
    except:
        return HttpResponse(404)
    book = {
        "id": getBook.id,
        "bookname": getBook.bookname,
        "originName": getBook.originName,
        "introduction": getBook.introduction,
        "author": getBook.author,
        "authorInfo": getBook.authorInfo,
        "authorPhoto": getBook.authorPhoto.url,
        "translator": getBook.translator,
        "press": getBook.press,
        "pressTime": getBook.pressTime.year,
        "page": getBook.page,
        "price": getBook.price,
        "label": getBook.label,
        "cover": getBook.cover.url,
        "star": star,
        "score": score,
        "all": allScoreComment
    }
    back["book"] = book

    try:
        getComment = Comment.objects.filter(book=getBook).order_by("-createTime")
        result = dividePage(request.GET, getComment)
        if result['pass']:
            back['pageCount'] = result['pageCount']
            getComment = result['output']
            back['nowPage'] = result['index'] - 1
    except:
        getComment = None
    c = {}
    if getComment:
        i = 0
        for comment in getComment:
            details = {
                "username": comment.owner.name,
                "commentId": comment.id,
                "content": comment.content,
                "score": comment.score,
                "praise": comment.praise,
                "time": comment.createTime
            }
            i = i + 1
            c[str(i)] = details
    back["comment"] = c

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            user = request.user
            logging.debug(user.name)
            score = form.cleaned_data["score"]
            logging.debug(score)
            newComment = Comment(book=getBook, owner=user, content=content, score=score)
            newComment.save()
        # 下面是点赞的
    form = CommentForm()
    back["form"] = form

    return render(request, "book_contain.html", back)


def book_new(request):
    return


def book_change(request):
    return


def book_delete(request):
    return


# def twice_label_choice(request, fLabelNum):
#     sLabel = Label.objects.filter(labelNum__range=(fLabelNum*100+1,fLabelNum*100+100))
#     result = []
#     for i in sLabel:
#         # 对应的id和ip组成一个字典
#         result.append({'id': i.labelNum, 'name': i.labelName})
#     # 返回json数据
#     return HttpResponse(json.dumps(result), content_type="application/json")