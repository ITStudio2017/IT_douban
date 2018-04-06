from django.db import models
from users.models import User
import logging


class Book(models.Model):
    # id
    bookname = models.CharField(verbose_name="书名", max_length=20)
    introduction = models.TextField(verbose_name="简介", max_length=500)
    createTime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    lastEditTime = models.DateTimeField(verbose_name="最后修改时间", auto_now=True)
    author = models.CharField(verbose_name="作者", max_length=30, default="")
    owner = models.ForeignKey(User, verbose_name="编辑人", editable=False, null=True, on_delete=models.CASCADE)
    label = models.IntegerField(verbose_name="标签", null=True)
    cover = models.ImageField(verbose_name="封面", upload_to='book_img')

    class Meta:
        verbose_name = r'图书'
        verbose_name_plural = r'图书'
        get_latest_by = "lastEditTime"

    def __str__(self):
        return self.bookname

    def get_father_labelname(self):
        try:
            return Label.objects.get(labelNum=self.label / 100).labelName
        except:
            pass

    def get_secondary_labelname(self):
        if self.label % 100 == 0:
            return None
        else:
            try:
                return Label.objects.get(labelNum=self.label).labelName
            except:
                pass


class Label(models.Model):
    # id
    labelName = models.CharField(max_length=10, verbose_name="标签名")
    labelNum = models.IntegerField(verbose_name="编号")

    class Meta:
        verbose_name = r'标签'
        verbose_name_plural = r'标签'
        get_latest_by = "labelNum"

    def __str__(self):
        f = self.get_fatherlabel_by_secondarylabel()
        result = ""
        if f:
            result = str(f.labelName) + ":"
        result = result + self.labelName
        return result

    def count_secondarylabel_by_fatherlabel(self):
        if self.labelNum < 100:
            return Label.objects.filter(labelNum__range=(self.labelNum * 100 + 1, (self.labelNum + 1) * 100)).count()
        else:
            return None

    def get_secondarylabel_by_fatherlabel(self):
        if self.labelNum < 100:
            return Label.objects.filter(labelNum__range=(self.labelNum * 100 + 1, (self.labelNum + 1) * 100))
        else:
            return None

    def get_fatherlabel_by_secondarylabel(self):
        if self.labelNum < 100:
            return None
        else:
            return Label.objects.get(labelNum=self.labelNum / 100)


def get_fatherlabel():
    return Label.objects.filter(labelNum__range=(1, 100))


def get_label_by_int(label: int=0):
    fLabel = None
    sLabel = None
    if label:
        if label in range(1, 100):
            try:
                fLabel = Label.objects.get(labelNum=label).labelName
            except:
                fLabel = None
        elif label > 100:
            try:
                fLabel = Label.objects.get(labelNum=label / 100).labelName
                sLabel = Label.objects.get(labelNum=label).labelName
            except:
                fLabel = None
                sLabel = None
    return fLabel, sLabel


def get_alllabel():
    back = {}
    fatherlabel = get_fatherlabel()
    for flabel in fatherlabel:
        sfnum = str(flabel.labelNum)
        back[sfnum] = {}
        back[sfnum]['fatherLabelInfo'] = flabel
        secondarylabel = flabel.get_secondarylabel_by_fatherlabel()
        back[sfnum]['secondaryLabel'] = {}
        for slabel in secondarylabel:
            ssnum = str(slabel.labelNum)
            back[sfnum]['secondaryLabel'][ssnum] = slabel
    return back


class Comment(models.Model):
    # id
    book = models.ForeignKey(Book, verbose_name="所在书目")
    owner = models.ForeignKey(User, verbose_name="评论人")
    content = models.CharField(max_length=200, verbose_name="内容")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = r'评论'
        verbose_name_plural = r'评论'
        get_latest_by = "createTime"

    def __str__(self):
        return self.book.bookname + ":" + self.content

