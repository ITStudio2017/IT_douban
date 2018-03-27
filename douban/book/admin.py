from django.contrib import admin
from .models import Book, Comment, Label

# Register your models here.
admin.site.register(Book)
admin.site.register(Label)
admin.site.register(Comment)
