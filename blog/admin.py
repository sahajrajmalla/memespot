from django.contrib import admin
from .models import Blog
# Register your models here.


class blogAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'date', 'meme_image')


admin.site.register(Blog, blogAdmin)
