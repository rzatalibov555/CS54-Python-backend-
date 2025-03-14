
from django.urls import path, re_path

from .views import * #all
# from news.views import about, contact, index

urlpatterns = [
    path("", index, name=""),
    path("index", index, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("error/", error, name="error"),
    path("allNews/", allNews, name="allNews"),

    path("news_detail/<int:post_id>/", news_detail, name="news_detail"),

    path('category/<int:cat_id>/', categories, name="category")

    # path('cats/<int:catId>', category),
    # re_path(r'^archive/(?P<year>[0-9]{4})/',archive),

    # path('cats/<int:catId>', category)
    # path('cats/<str:catId>', category)
    # path('cats/<uuid:catId>', category),
    # path('cats/<path:catId>', category),
]

