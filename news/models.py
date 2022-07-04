from statistics import mode
from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=180)
    url = models.CharField(max_length=200, unique=True)
    pub_date = models.CharField(max_length=50)
    body = models.TextField()
    site = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        managed = True

class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return "Image for: " + self.news.title + ". Url: " + self.image_url

    class Meta:
        managed = True