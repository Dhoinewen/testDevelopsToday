from django.contrib import admin
from .models import Post, Comments


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Comments)
