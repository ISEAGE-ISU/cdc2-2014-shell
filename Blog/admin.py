from django.contrib import admin
from Blog.models import Post

# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

admin.site.register(Post, postAdmin)