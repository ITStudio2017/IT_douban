from django.shortcuts import render
import json
from django.shortcuts import redirect
from users.models import User
from .forms import *
from .models import *
from django.db.models import Q
from book.models import Book, Collection
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.files.base import ContentFile
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
import logging
from django.core.paginator import EmptyPage
from django.shortcuts import render_to_response
from book.models import Comment as bookComment

def userPage(request):
    article_list = Article.objects.filter(isHomeArticle=True).order_by('-update_time')[:11]
    article_1 = article_list[:1]
    article_2 = article_list[1:2]
    article_3 = article_list[2:3]
    article_4 = article_list[3:4]
    article_5 = article_list[4:5]
    article_photo = article_list[5:7]
    article_list = article_list[7:11]
    logging.debug(article_1)

    back = {
        "book": {},
        'article_list': article_list,
        'article_photo': article_photo,
        'article_1': article_1,
        'article_2': article_2,
        'article_3': article_3,
        'article_4': article_4,
        'article_5': article_5,
    }
    books = Book.objects.all().order_by('-score')[:8]
    i = 0
    allBook = {}
    for book in books:
        i = i + 1
        count = Collection.objects.filter(book=book).count()
        allBook[str(i)] = {
            "id": book.id,
            "score": book.score,
            "cover": book.cover.url,
            "bookname": book.bookname,
            "loveCount": count,
        }
    logging.debug(allBook)
    back['book'] = allBook
    try:
        first = request.user.first_login
    except:
        return render(request, 'shouye.html', back)

    logging.debug("11111111111111111111")

    if first == True:
        return render(request, 'main/personal_change.html')

    return render(request, 'shouye.html', back)


def userInformation(request):
    if not request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        user.name = request.POST['name']
        user.sex = request.POST['sex']
        user.motto = request.POST['motto']
        user.head_img = request.FILES['image']
        user.first_login = False
        user.save()
    else:
        return render(request, 'main/personal_change.html')
    return redirect('/')


def WriteArticle(request):
    if not request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return render(request, 'main/personal_center_write_article.html')
        else:
            return render(request, 'main/personal_center_write_article.html')
    else:
        return render(request, 'main/personal_center_write_article.html')


def userArticle(request):
    if not request.user.is_authenticated():
        return redirect('/')
    article_list = Article.objects.filter(author=request.user).order_by('-update_time')
    return render(request, 'main/personal_center_personal_article.html', {'article_list': article_list})


def deleteArticle(request, id):
    if not request.user.is_authenticated():
        return redirect('/')
    user = request.user
    article = Article.objects.get(id=id,author=user)
    comment = comment_article.objects.filter(article=article)
    article.delete()
    comment.delete()
    return redirect('/userArticleList/')


def changeArticle(request, id):
    if not request.user.is_authenticated():
        return redirect('/')
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES, instance=article)
        if form.is_valid():
            j = form.save(commit=False)
            j.save()
            return redirect('/userArticleList/')
    else:
        return render(request, 'main/personal_change_article.html', {'article': article})


def article_detail(request, id):
    art = Article.objects.get(id=id)
    art.increase_views()
    commentOfArticle = comment_article.objects.filter(article=art).order_by('-pub_date')
    if request.user.is_authenticated():
        shoucang_list = article_save.objects.filter(article=art)
        isSave = False
        for i in shoucang_list:
            if i.user == request.user:
                isSave = True

        if request.method == 'POST':
            commentForm = Comment_Article_Form(request.POST)
            if commentForm.is_valid():
                comment = commentForm.save(commit=False)
                comment.author = request.user
                comment.article = art
                comment.save()
        return render(request, 'main/article_contain.html',
                      {'isSave': isSave, 'article': art, 'commentOfArticle': commentOfArticle})
    else:
        return render(request, 'main/article_contain.html', {'article': art, 'commentOfArticle': commentOfArticle})


def commentList(request):
    articleCommentList = comment_article.objects.filter(author=request.user).order_by('-pub_date')
    bookCommentList = bookComment.objects.filter(owner_id=request.user.id).order_by('-createTime')
    return render(request, 'main/personal_center_comment.html', {
        'articleCommentList': articleCommentList,
        'bookCommentList':bookCommentList})


def articleCate(request, cate, page):
    if cate == '1':
        article_list = Article.objects.all().filter(isDisplay = True).order_by('-views')[:15]
    elif cate == '2':
        article_list = Article.objects.all().filter(isDisplay = True).order_by('-update_time')[:15]
    elif cate == '3':
        article_list = Article.objects.filter(isDisplay = True).filter(article_cate='小说').order_by('-update_time')[:15]
    elif cate == '4':
        article_list = Article.objects.filter(isDisplay = True).filter(article_cate='散文').order_by('-update_time')[:15]
    elif cate == '5':
        article_list = Article.objects.filter(isDisplay = True).filter(article_cate='感悟').order_by('-update_time')[:15]
    elif cate == '6':
        article_list = Article.objects.filter(isDisplay = True).filter(article_cate='新闻').order_by('-update_time')[:15]
    else:
        cate = '1'
    paginator = Paginator(article_list, 5)
    try:
        article_page = paginator.page(page)
    except:
        page = 1
        article_page = paginator.page(page)
    if not request.user.is_authenticated():
        if request.method == 'POST':
            message = '请登录后收藏!'
            return render(request, 'main/article_list.html',
                          {'message': message, 'cate': cate, 'article_page': article_page})
        return render(request, 'main/article_list.html', {'cate': cate, 'article_page': article_page})
    else:
        save_article = article_save.objects.filter(user=request.user)
        if request.method == 'POST':
            article_id = request.POST['article_id']
            article = Article.objects.get(pk=article_id)
            try:
                article_save.objects.filter(article=article).get(user=request.user)
                message = '请勿重复收藏！'
                return render(request, 'main/article_list.html',
                              {'cate': cate, 'article_page': article_page, 'save_article': save_article,
                               'message': message})
            except:
                isSave = article_save()
                isSave.user = request.user
                isSave.article = article
                isSave.save()
                return render(request, 'main/article_list.html',
                              {'cate': cate, 'article_page': article_page, 'save_article': save_article})
    return render(request, 'main/article_list.html',
                  {'cate': cate, 'article_page': article_page, 'save_article': save_article})


def article_shoucang(request, article_id):
    article = Article.objects.get(id=article_id)
    commentOfArticle = comment_article.objects.filter(article=article).order_by('-pub_date')
    if not request.user.is_authenticated():
        message = '请登录后收藏!'
        return render(request,'main/article_contain.html',{'article':article,'message':message})
    else:
        if request.method == 'POST':
            article_id = request.POST['article_id']
            article = Article.objects.get(pk=article_id)
            try:
                article_save.objects.filter(article=article).get(user=request.user)
                message = '请勿重复收藏！'
                return redirect('/detail/' + article_id + '/')
            except:
                isSave = article_save()
                isSave.user = request.user
                isSave.article = article
                isSave.save()
                return redirect('/detail/' + article_id + '/')


def saveArticle(request):
    if not request.user.is_authenticated():
        return redirect('/')
    save_list = article_save.objects.filter(user=request.user).order_by('-time')
    return render(request, 'main/personal_center_save_article.html', {'save_list': save_list})


def deleteSave(request, article_id):
    if not request.user.is_authenticated():
        return redirect('/')
    article = Article.objects.get(id=article_id)
    saveArticle = article_save.objects.get(article=article)
    saveArticle.delete()
    return redirect('/saveArticle/')

def deleteComment(request,comment_id):
    if not request.user.is_authenticated():
        return redirect('/')
    comment = comment_article.objects.get(pk=comment_id)
    comment.delete()
    return redirect('/comment/')



def display_book_collect(request):
    back = {
        "book":{},
    }
    allC = Collection.objects.filter(collector=request.user)
    books = {}
    i = 0
    for c in allC:
        i = i + 1
        book = c.book
        books[str(i)] = {
            "id": book.id,
            "cover": book.cover.url,
            "bookname": book.bookname,
        }
    back["book"] = books
    return render(request, 'main/personal_center_save_book.html', back)

def searchArticle(request):
    try:
        page = request.GET['page']
    except:
        page = 1
    try:
        page = int(page)
    except:
        return redirect('/')
    try:
        st = request.GET['keyword']
    except:
        return redirect('/')
    allArticle = Article.objects.filter(Q(title__contains=st) | Q(content__contains=st))
    if not allArticle:
        return render(request,'main/search.html',{'message':"结果为空！"})
    articleList = allArticle.order_by('-views')
    paginator = Paginator(articleList, 5)
    try:
        articleList = paginator.page(page)
        lastPage = page - 1
        nextPage = page + 1
    except EmptyPage:
        articleList = paginator.page(1)
        page = 1
        lastPage = 1
        nextPage = 1
    
    return render(request,'main/search.html',{
        'articleList':articleList,
        'keyword':st,
        'page':page,
        'lastPage':lastPage,
        'nextPage':nextPage
        })

def page_not_found(request):
    return render_to_response('404_error.html')
# Create your views here.
