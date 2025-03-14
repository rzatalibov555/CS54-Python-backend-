from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render
from .models import Category, News 
from django.db.models import Count
# Create your views here.

menu = [
        {'title': "Home", "url_name":"home"},
        {'title': "About", "url_name":"about"},
        {'title': "Contact", "url_name":"contact"},
    ]

def index(request):

    context = {
        "title":"Home",
        "posts" : News.objects.all(),
        "cat_selected" : 0,

        "categories" : Category.objects.all(),
        "menu": menu,
    }

    return render(request, "news/index.html", context)

def categories(request, cat_id):

    news = News.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(news) == 0:
        raise Http404()

    context = {
        "title": "Category",
        "news" : news,
        "cats" : cats,
        "cat_selected" : cat_id,

        "categories" : Category.objects.all(),
        "menu": menu
    }

    return render(request, "news/life-style.html", context=context)
    # return HttpResponse(f"Category - {cat_id}")

def about(request):
    context = {
        "title": "About",

        "categories" : Category.objects.all(),
        "menu": menu
    }
    return render(request, "news/about-us.html", context=context)

def contact(request):
    context = {
        "title": "Contact",

        "categories" : Category.objects.all(),
        "menu": menu
    }
    return render(request, "news/contact-us.html", context=context)

def allCategories(request):
    pass

def allNews(request):
    
    context = {
        "title": "All news",
        "news" : News.objects.all(),
        "categories" : Category.objects.all(),
        "menu": menu
    }
    return render(request, "news/all_news.html",context)


def news_detail(request, post_id):
    
    news_detail = News.objects.get(id=post_id)

    related_news = News.objects.filter(cat=news_detail.cat).exclude(id=news_detail.id)[:6]
  
    
    categories = Category.objects.annotate(news_count=Count('news')).filter(news_count__gt=0)

    context = {
        "title": "Detail news",
        "news" : news_detail,
        "related_news": related_news,
        "news_limit" : News.objects.order_by('-id').exclude(id=news_detail.id)[:5],
        "categories" : categories,
        "menu": menu
    }
    
    return render(request, "news/detail_news.html", context)



def error(request):
    context = {
        "title":"Error"
    }
    return render(request, "news/error.html", context)

def pageNotFound(request, exception):
    return HttpResponseNotFound("UPSSS! Sehife tapilmadi")

# def index(request):
#     return HttpResponse("<h1>Home page</h1>")

# def about(request):
#     return HttpResponse("<h1>About page</h1>")

# def contact(request):
#     return HttpResponse("Contact page")

# def category(request, catId):
#     if request.GET:
#         print(request.GET)
#     return HttpResponse(f"{catId} Kateqoriya")

# def archive(request, year):
#     if int(year) > 2024:
#         raise Http404()
#     return HttpResponse(f"Arxivde {year} wzre axtaris")

