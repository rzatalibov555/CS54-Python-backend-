from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        "title":"Home", 
        "user":"Muradik",
        "menu": ["Home", "About", "Contact"]
    }

    return render(request, "news/index.html", context)


def about(request):
    return render(request, "news/about.html", {"title":"About", "user":"Ayxan"})

def contact(request):
    return render(request, "news/contact.html", {"title":"Contact", "user":"Muradik"})





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

def pageNotFound(request, exception):
    return HttpResponseNotFound("UPSSS! Sehife tapilmadi")