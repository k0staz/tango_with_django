from django.contrib import admin
from rango.models import Category, Page

class PagesInLine(admin.TabularInline):
    model = Page
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Statistic', {'fields': ['views', 'likes'], 'classes': ['collapse']}),
    ]
    inlines = [PagesInLine]
    list_display = ('name', 'views', 'likes')
    list_filter = ['views', 'likes']
    search_fields = ['name']

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)