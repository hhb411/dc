from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models


# 文章列表页面
def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles':articles})


# 文章显示页面
def article_page(request, article_id):
    # article_id = request.GET['article_id']
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article.html', {'article': article})


# 文章编辑页面
def article_edit_page(request):
    insert_tag = request.GET['insert_tag']
    if insert_tag == '1':
        # insert
        return render(request, 'blog/edit_article.html', {'insert_tag': insert_tag})
    else:
        # edit
        article_id = request.GET['article_id']
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'blog/edit_article.html', {'insert_tag': insert_tag, 'article': article})


# 文章修改提交
def article_edit_action(request):
    insert_tag = request.POST['insert_tag']# 插入/编辑 标志
    article_id = request.POST['article_id']
    if insert_tag == '1':
        # insert
        article = models.Article.objects.create()
    else:
        # edit
        article = models.Article.objects.get(pk=article_id)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    return HttpResponseRedirect('articles/' + str(article.id)
    return  render(request, 'blog/article.html', {'article': article})
