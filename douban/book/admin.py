from django.contrib import admin
from .models import Book, Comment, Label


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('bookname', 'author', 'label')
    fieldsets = (
        [u'主要信息', {
            'fields': ('bookname', 'author', 'introduction'),
        }],
        [u'附加', {
            'fields': ('label', 'cover'),
        }]
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Label)
admin.site.register(Comment)
