# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-06 01:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='\u4f5a\u540d', max_length=20, verbose_name='\u4f5c\u8005')),
                ('bookName', models.CharField(max_length=20, verbose_name='\u4e66\u540d')),
                ('coverImg', models.ImageField(default='./2706179_185025082_2.jpg', upload_to=b'', verbose_name='\u4e66\u7c4d\u5c01\u9762')),
                ('describe', models.TextField(verbose_name='\u4e66\u7c4d\u6982\u8981\u7b80\u4ecb')),
                ('type', models.SmallIntegerField(choices=[(1, '\u4ed9\u5251'), (2, '\u7384\u5e7b'), (3, '\u60ac\u7591'), (4, '\u5947\u5e7b'), (5, '\u519b\u4e8b'), (6, '\u5386\u53f2'), (7, '\u7ade\u6280'), (8, '\u79d1\u5e7b'), (9, '\u519b\u4e8b'), (10, '\u6821\u56ed'), (11, '\u793e\u4f1a'), (12, '\u5176\u5b83')], default=1, verbose_name='\u4e66\u7c4d\u7c7b\u578b')),
                ('wordNumber', models.IntegerField(default=0, verbose_name='\u5b57\u6570')),
                ('state', models.SmallIntegerField(choices=[(0, '\u66f4\u65b0\u4e2d'), (1, '\u5df2\u5b8c\u6210')], default=0, verbose_name='\u66f4\u65b0\u72b6\u6001')),
                ('chaptersNumber', models.SmallIntegerField(default=0, verbose_name='\u66f4\u65b0\u7ae0\u8282\u6570')),
                ('bookMoney', models.IntegerField(default=0, verbose_name='\u4e66\u7c4d\u4ef7\u683c')),
                ('updateTime', models.DateTimeField(auto_now_add=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('clicksNumber', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u91cf')),
                ('subscribersNumber', models.IntegerField(default=0, verbose_name='\u8ba2\u9605\u91cf')),
                ('chaseBooksNumber', models.IntegerField(default=0, verbose_name='\u8ffd\u4e66\u91cf')),
                ('reward', models.IntegerField(default=0, verbose_name='\u732b\u5e01\u6253\u8d4f\u603b\u6570')),
                ('catBallNumber', models.IntegerField(default=0, verbose_name='\u732b\u7403\u6253\u8d4f\u603b\u91cf')),
                ('catnipNumber', models.IntegerField(default=0, verbose_name='\u732b\u8584\u8377\u6253\u8d4f\u603b\u91cf')),
                ('catStickNumber', models.IntegerField(default=0, verbose_name='\u9017\u732b\u68d2\u6253\u8d4f\u603b\u91cf')),
                ('catFoodNumber', models.IntegerField(default=0, verbose_name='\u732b\u6293\u996d\u6253\u8d4f\u603b\u91cf')),
                ('catFishNumber', models.IntegerField(default=0, verbose_name='\u8dd1\u722c\u67b6\u6253\u8d4f\u603b\u91cf')),
                ('catHouseNumber', models.IntegerField(default=0, verbose_name='\u732b\u7a9d\u6253\u8d4f\u603b\u91cf')),
            ],
            options={
                'db_table': 'book_info',
            },
        ),
        migrations.CreateModel(
            name='BooksContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chaptersId', models.SmallIntegerField(verbose_name='\u7ae0\u8282\u6570')),
                ('chaptersName', models.CharField(max_length=20, verbose_name='\u7ae0\u8282\u540d\u79f0')),
                ('chaptersContent', models.TextField(verbose_name='\u7ae0\u8282\u5185\u5bb9')),
                ('wordNumber', models.IntegerField(default=0, verbose_name='\u7ae0\u8282\u5b57\u6570')),
                ('updateTime', models.DateTimeField(auto_now_add=True, verbose_name='\u7ae0\u8282\u66f4\u65b0\u65f6\u95f4')),
                ('chaptersType', models.IntegerField(choices=[(0, '\u514d\u8d39'), (1, '\u6536\u8d39')], default=0, verbose_name='\u7ae0\u8282\u7c7b\u578b')),
                ('chaptersState', models.IntegerField(choices=[(0, '\u4e0d\u53d1\u5e03'), (1, '\u53d1\u5e03')], default=0, verbose_name='\u7ae0\u8282\u7c7b\u578b')),
                ('chaptersMoney', models.IntegerField(default=0, verbose_name='\u7ae0\u8282\u4ef7\u94b1')),
                ('chaptersPV', models.IntegerField(default=0, verbose_name='\u7ae0\u8282\u6d4f\u89c8\u91cf')),
                ('BookInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookinfo_bookscontent', to='books.BookInfo', verbose_name='\u4e66\u672cID')),
            ],
            options={
                'db_table': 'book_content',
            },
        ),
    ]
