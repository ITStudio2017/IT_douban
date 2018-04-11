# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-11 19:19
from __future__ import unicode_literals

import DjangoUeditor.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='内容')),
                ('abstract', models.CharField(blank=True, max_length=256, null=True, verbose_name='摘要')),
                ('article_cate', models.CharField(choices=[('小说', '小说'), ('散文', '散文'), ('戏曲', '戏曲'), ('剧本', '剧本'), ('诗歌', '诗歌'), ('寓言', '寓言'), ('童话', '童话'), ('书信', '书信'), ('议论文', '议论文'), ('说明文', '说明文'), ('记叙文', '记叙文'), ('报告', '报告'), ('总结', '总结'), ('新闻', '新闻')], default='小说', max_length=5, verbose_name='类别')),
                ('views', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(storage=main.storage.ImageStorage(), upload_to='article_img', verbose_name='封面')),
                ('sort', models.PositiveIntegerField(default='1')),
                ('author', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '用户文章',
                'verbose_name_plural': '用户文章',
            },
        ),
        migrations.CreateModel(
            name='article_save',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('article', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.Article')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '文章收藏',
                'verbose_name_plural': '文章收藏',
            },
        ),
        migrations.CreateModel(
            name='comment_article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=145, verbose_name='内容')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('article', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.Article')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '文章评论',
                'verbose_name_plural': '文章评论',
            },
        ),
    ]
