from django.db import models
from DjangoUeditor.models import UEditorField
from users.models import User
from django.utils.html import strip_tags
from .storage import ImageStorage


class Article(models.Model):
    category=(('小说','小说'),('散文','散文'),('戏曲','戏曲'),('剧本','剧本'),('诗歌','诗歌'),('寓言','寓言'),('童话','童话'),('书信','书信'),('议论文','议论文'),('说明文','说明文'),('记叙文','记叙文'),('报告','报告'),('总结','总结'),('新闻','新闻'),)
    title = models.CharField('标题',max_length=256)
    pub_date = models.DateTimeField('发表时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间',auto_now=True,null=True)
    content = UEditorField('内容',toolbars="full",upload_settings={"imageMaxSize":1204000},settings={},)
    author = models.ForeignKey(User,default="",)
    abstract = models.CharField('摘要',max_length=256,null=True,blank=True)
    article_cate = models.CharField('类别',max_length=5,choices=category,default='小说')
    views = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='article_img',storage=ImageStorage())

    def save(self,*args,**kwargs):
        if not self.abstract:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                ])
            self.abstract = strip_tags(md.convert(self.content))[:54]
        super(Article,self).save(*args,**kwargs)
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = r"所有图书"
        verbose_name_plural = r"所有图书"

    
class comment_article(models.Model):
    content = models.CharField('内容',max_length=145)
    pub_date = models.DateTimeField('发表时间',auto_now_add=True)
    author = models.ForeignKey(User, default="")
    article = models.ForeignKey(Article,default="")
    class Meta:
        verbose_name = r"图书评论"
        verbose_name_plural = r"图书评论"
        
    

class article_save(models.Model):
    article = models.ForeignKey(Article,default="")
    user = models.ForeignKey(User,default="")
    time = models.DateTimeField('时间',auto_now_add=True)
    class Meta:
        verbose_name = r"图书收藏"
        verbose_name_plural = r"图书收藏"

# Create your models here.
