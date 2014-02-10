from django.contrib import admin
from Blog.models import Post

# Register your models here.
class postAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Post, postAdmin)