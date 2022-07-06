from django.db import models

# Create your models here.
class Crawler(models.Model):
    name = models.CharField(max_length=100)
    allowed_domain = models.CharField(max_length=100)
    start_url = models.CharField(max_length=180)
    start_url_search = models.CharField(max_length=180)
    url = models.CharField(max_length=180)
    css_all_newsdiv = models.CharField(max_length=180)
    css_search_newsdiv = models.CharField(max_length=180)
    title_css = models.CharField(max_length=180)
    pub_date_css = models.CharField(max_length=180)
    body_css = models.CharField(max_length=180)
    image_xpath = models.CharField(max_length=180)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
