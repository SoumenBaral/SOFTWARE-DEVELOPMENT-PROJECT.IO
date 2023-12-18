from django.contrib import admin
from . import models
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('Name',)}
    list_display = ['Name', 'slug']
    
admin.site.register(models.Brand, BrandAdmin)