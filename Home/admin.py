from django.contrib import admin
from Home.models import client

# Register your models here.
class clientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'ach_payment_info', 'site_name')

admin.site.register(client, clientAdmin)