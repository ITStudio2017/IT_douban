from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
	"""docstring for A"""
	list_display=('title','pub_date','update_time',)

	
		

# Register your models here.
admin.site.register(Article,ArticleAdmin)