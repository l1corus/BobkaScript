from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    search_fields = ['pk', 'title']
    list_display_links = ['pk', 'title']


admin.site.register(Post, PostAdmin)
