from django.contrib import admin
from .models import Book, Comment, Label


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['bookname', 'author', 'fsLabel']
    search_fields = ['bookname']

    fieldsets = (
        [u'主要信息', {
            'fields': ('bookname', 'author', 'introduction', 'owner'),
        }],
        [u'附加', {
            'fields': ('label', 'cover'),
        }]
    )

    def fsLabel(self, obj):
        fLabel = obj.get_father_labelname()
        sLabel = obj.get_secondary_labelname()
        retstr = ""
        if fLabel:
            retstr = retstr + fLabel
            if sLabel:
                retstr = retstr + ":" + sLabel
        return str(retstr)
    fsLabel.short_description = "标签"


class CommentAdmin(admin.ModelAdmin):
    list_display = ['book', 'owner', 'createTime']


class LabelAdmin(admin.ModelAdmin):
    list_display = ['labelName', 'labelNum', 'fLabel']
    search_fields = ['labelName']

    def fLabel(self, obj):
        fLabel = obj.get_fatherlabel_by_secondarylabel()
        retstr = ""
        if fLabel:
            retstr = retstr + fLabel.labelName
        return str(retstr)
    fLabel.short_description = "父标签"


admin.site.register(Book, BookAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Comment, CommentAdmin)
