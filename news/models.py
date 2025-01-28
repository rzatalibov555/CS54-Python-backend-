from django.db import models
from django.urls import reverse

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Başlıq")
    description = models.TextField(blank=True, verbose_name="Kontent")
    image = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name="Şəkİl")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Yaranma tarİxİ")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yenİlənmə tarİxİ")
    is_published = models.BooleanField(default=True, verbose_name="Status")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
        # return  str(self.is_published)

        

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering =['time_create','title']

    # def get_absolute_url(self):
    #     return reverse("news_detail", kwargs={"news_id": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=60, db_index=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Yaranma tarİxİ")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yenİlənmə tarİxİ")
    is_published = models.BooleanField(default=True, verbose_name="Status")


    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk})
    