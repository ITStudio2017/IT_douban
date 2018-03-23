from django.db import models
import logging


class Book(models.Model):
    # id
    bookname = models.CharField(max_length=20)
    introduction = models.TextField(max_length=500)
    createTime = models.DateTimeField(auto_now_add=True)
    lastEditTime = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=30, default="")
    owner = models.IntegerField()
    label = models.IntegerField(null=True)
    cover = models.ImageField(upload_to='book_img')

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
    labelName = models.CharField(max_length=10)
    labelNum = models.IntegerField()

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
