from django.contrib import admin
from .models import Journal, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Journal)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'news', 'news_events')
    search_fields = ['title', 'news']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)