from django.shortcuts import render
import json
from django.shortcuts import redirect
from users.models import User
from .forms import ArticleForm,Comment_Article_Form
from .models import Article,comment_article
from django.http import HttpResponseRedirect 
from django.template.loader import render_to_string
from django.core.files.base import ContentFile
from django.core.paginator import Paginator

def userPage(request):
	article_list= Article.objects.all().order_by('-views')[:11]
	article_1 = article_list[:1]
	article_2 = article_list[1:2]
	article_3 = article_list[2:3]
	article_4 = article_list[3:4]
	article_5 = article_list[4:5]
	article_photo = article_list[5:7]
	article_list = article_list[7:11]
	try:
		first = request.user.first_login;
	except:
		return render(request,'shouye.html',{'article_list':article_list,'article_photo':article_photo,
			'article_1':article_1,
			'article_2':article_2,
			'article_3':article_3,
			'article_4':article_4,
			'article_5':article_5})
	
	if(first == True):
		return render(request,'main/account_profile.html')
	else:
		return render(request,'shouye.html',{'article_list':article_list,'article_photo':article_photo,
			'article_1':article_1,
			'article_2':article_2,
			'article_3':article_3,
			'article_4':article_4,
			'article_5':article_5})


def userInformation(request):
	if request.method == 'POST':
		a = json.loads(request.body)
		b = User.objects.get(email=request.user.email)
		b.name = a['name']
		b.sex = a['sex']
		b.first_login=False
		b.save()
	return render(request,'main/index.html')

def WriteArticle(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
        	article = form.save(commit=False)
        	article.author = request.user
        	article.save()
        	return render(request,'main/personal_center_write_article.html')
    else:
        form = ArticleForm()
        return render(request,'main/personal_center_write_article.html',{'form':form})
            
def userArticle(request):
	article_list = Article.objects.filter(author=request.user).order_by('-update_time')
	return render(request,'main/personal_center_personal_article.html',{'article_list':article_list})

def deleteArticle(request,id):
	article = Article.objects.get(id = id)
	comment = comment_article.objects.filter(article=article)
	article.delete()
	comment.delete()
	article_list = Article.objects.filter(author=request.user)
	return render(request,'main/personal_center_personal_article.html',{'article_list':article_list})
	
def changeArticle(request,id):
	article = Article.objects.get(id=id)
	if request.method == 'POST':
		form = ArticleForm(request.POST,instance=article)
		if form.is_valid():
			j = form.save(commit=False)
			j.save()
			return redirect('/userArticleList/')
	else:
		return render(request,'main/personal_change_article.html',{'article':article})

def article_detail(request,id):
	art = Article.objects.get(id=id)
	commentOfArticle = comment_article.objects.filter(article=art).order_by('-pub_date')
	if request.method == 'POST':
		commentForm = Comment_Article_Form(request.POST)
		if commentForm.is_valid():
			comment = commentForm.save(commit=False)
			comment.author = request.user
			comment.article = art
			comment.save()
			commentForm = Comment_Article_Form()
			return render(request,'main/article_contain.html',{'article':art,'commentForm':commentForm,'commentOfArticle':commentOfArticle})
	else:
		commentForm = Comment_Article_Form()
		return render(request,'main/article_contain.html',{'article':art,'commentForm':commentForm,'commentOfArticle':commentOfArticle})

def commentList(request):
	commentList = comment_article.objects.filter(author=request.user).order_by('-pub_date')
	return render(request,'main/personal_center_comment.html',{'commentList':commentList})

def articleList(request,page):
	article_list = Article.objects.all().order_by('-views')[:15]
	paginator = Paginator(article_list,5)
	article_page = paginator.page(page)
	return render(request,'main/article_list.html',{'article_page':article_page})

def newArticleList(request,page):
	article_list = Article.objects.all().order_by('-update_time')[:15]
	paginator = Paginator(article_list,5)
	article_page = paginator.page(page)
	return render(request,'main/article_list_new.html',{'article_page':article_page})

def articleCate(request,cate,page):
	if cate == '1':
		article_list = Article.objects.filter(article_cate='小说')[:15]
	if cate == '2':
		article_list = Article.objects.filter(article_cate='散文')[:15] 
	if cate == '3':
		article_list = Article.objects.filter(article_cate='感悟')[:15]
	if cate == '4':
		article_list = Article.objects.filter(article_cate='新闻')[:15]
	paginator = Paginator(article_list,5)
	article_page = paginator.page(page)
	content = {'article_page':article_page,'cate':cate}
	return render(request,'main/article_list_cate.html',content)

# Create your views here.
