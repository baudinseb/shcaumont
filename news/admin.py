from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display   = ('title', 'author', 'pub_date')
    list_filter    = ('author', )
    ordering       = ('pub_date', )
    search_fields  = ('title', 'text')

admin.site.register(News, NewsAdmin)

# Register your models here.
