from django.conf.urls import url
from .views import (WriteArticl,userInformation,userPage,userArticle,
        deleteArticle,changeArticle,article_detail,commentList)

urlpatterns = [
    url(r'^write/',WriteArticl,name='WriteArticl'),
    url(r'^informationChange/',userInformation),
    url(r'^$',userPage),
    url(r'^index/',userPage),
    url(r'^userArticleList/',userArticle,name='userArticle'),
    url(r'^delete/(?P<id>[0-9]+)/$',deleteArticle,name='deleteArticle'),
    url(r'^change/(?P<id>[0-9]+)/$',changeArticle,name='changeArticle'),
    url(r'^detail/(?P<id>[0-9]+)/$',article_detail,name='article_detail'),
    url(r'^comment/$',commentList,name='commentList'),
]
