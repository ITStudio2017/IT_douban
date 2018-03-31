from django.db import models
from DjangoUeditor.models import UEditorField
from users.models import User

class Article(models.Model):
    category=(('小说','小说'),('散文','散文'),('戏曲','戏曲'),('剧本','剧本'),('诗歌','诗歌'),('寓言','寓言'),('童话','童话'),('书信','书信'),('议论文','议论文'),('说明文','说明文'),('记叙文','记叙文'),('报告','报告'),('总结','总结'),('新闻','新闻'),)
    title = models.CharField('标题',max_length=256)
    pub_date = models.DateTimeField('发表时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间',auto_now=True,null=True)
    content = UEditorField('内容',toolbars="full", imagePath="static/img/", filePath="main/static/img/", upload_settings={"imageMaxSize":1204000},settings={},)
    author = models.ForeignKey(User)
    abstract = models.CharField('摘要',max_length=256,null=True,blank=True)
    article_cate = models.CharField('类别',max_length=5,choices=category,default='小说')
    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    

    
# Create your models here.
