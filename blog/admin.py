from django.contrib import admin
from models import Category, Page, Userpro

class CategoryAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
admin.site.register(Userpro)