from django.shortcuts import render
import json
from users.models import User

def index(request):
    return render(request,'basemain.html')

def userPage(request):
	first = request.user.first_login;
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

# Create your views here.
