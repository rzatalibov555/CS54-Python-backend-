
from django.urls import path, re_path

from .views import * #all
# from news.views import about, contact, index

urlpatterns = [
    path("", index),
    path("index", index),
    path("about/", about),
    path("contact/", contact),
    # path('cats/<int:catId>', category),
    # re_path(r'^archive/(?P<year>[0-9]{4})/',archive),

    # path('cats/<int:catId>', category)
    # path('cats/<str:catId>', category)
    # path('cats/<uuid:catId>', category),
    # path('cats/<path:catId>', category),
]

