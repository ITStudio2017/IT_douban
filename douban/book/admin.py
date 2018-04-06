from django.contrib import admin
from .models import Book, Comment, Label, Praise, Collection
import datetime
import logging


class BookTimeModelFilter(admin.SimpleListFilter):
    title = r'创建时间'
    parameter_name = r'创建时间'

    def lookups(self, request, model_admin):
        now = datetime.datetime.now()
        yearago = now - datetime.timedelta(days=365)
        monthago = now - datetime.timedelta(days=30)
        dayago = now - datetime.timedelta(days=1)
        return [
            (dayago, r"一天内"),
            (monthago, r"一月内"),
            (yearago, r"一年内"),
        ]

    def queryset(self, request, queryset):
        now = datetime.datetime.now()
        try:
            value = self.value()
        except:
            value = None
        if value:
            return queryset.filter(lastEditTime__range=(value, now))
        else:
            return queryset


class BookAdmin(admin.ModelAdmin):
    list_display = ['bookname', 'author', 'fsLabel', 'owner']
    list_filter = (BookTimeModelFilter,)
    search_fields = ['bookname', 'author']

    fieldsets = (
        [u'主要信息', {
            'fields': ('bookname', 'author', 'introduction'),
        }],
        [u'附加', {
            'fields': ('label', 'cover'),
        }]
    )

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        logging.debug(request.user)
        obj.save()

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
        f = obj.get_fatherlabel_by_secondarylabel()
        retstr = ""
        if f:
            retstr = retstr + f.labelName
        return str(retstr)
    fLabel.short_description = "父标签"


admin.site.register(Book, BookAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Praise)
admin.site.register(Collection)
