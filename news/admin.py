from django.contrib import admin
from .models import News, NewsImage

# Register your models here.
class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 0


class NewsAdmin(admin.ModelAdmin):
    model = News
    inlines = [NewsImageInline]
    list_filter = ["pub_date"]
    search_fields = ["title", "body"]


admin.site.register(News, NewsAdmin)
