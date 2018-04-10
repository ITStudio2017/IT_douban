from django.contrib import admin
from .models import *

admin.site.site_header = '豆瓣读书管理系统'
admin.site.site_title = '豆瓣管理'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','pub_date','update_time',)
	search_fields = ('title','content')
	list_per_page = 10



@admin.register(comment_article)
class Comment_article(admin.ModelAdmin):
	list_display=('id','author','article')
	list_display_links = ('id','author','article')

@admin.register(article_save)
class Save_Article(admin.ModelAdmin):
	list_display = ('id','user','article')
	


		

