from django.shortcuts import render
import json
from users.models import User
from .forms import ArticleForm
from .models import Article

def userPage(request):
	try:
		first = request.user.first_login;
	except:
		return render(request,'main/index.html')
	
	if(first == True):
		return render(request,'main/account_profile.html')
	else:
		return render(request,'main/index.html')


def userInformation(request):
	if request.method == 'POST':
		a = json.loads(request.body)
		b = User.objects.get(email=request.user.email)
		b.name = a['name']
		b.sex = a['sex']
		b.first_login=False
		b.save()
	return render(request,'main/index.html')

def WriteArticl(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
        	article = form.save(commit=False)
        	article.author = request.user
        	article.save()
        	return render(request,'main/personal_center_write_article.html')
    else:
        form = ArticleForm()
        return render(request,'main/personal_center_write_article.html',{'form':form})
            
def userArticle(request):
	article_list = Article.objects.filter(author=request.user)
	return render(request,'main/personal_center_personal_article.html',{'article_list':article_list})
# Create your views here.
