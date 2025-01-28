from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render
from .models import Category, News 

# Create your views here.

def index(request):

    context = {
        "title":"Home",
        "posts" : News.objects.all()
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
        "cat_selected" : cat_id
    }

    return render(request, "news/life-style.html", context=context)
    # return HttpResponse(f"Category - {cat_id}")

def about(request):
    return render(request, "news/about.html", {"title":"About"})

def contact(request):
    return render(request, "news/contact-us.html", {"title":"Contact"})


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

