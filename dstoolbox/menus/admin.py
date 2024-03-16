from django.contrib import admin
from main.models import Menu , Category
# Register your models here.

class MenusAdmin(admin.ModelAdmin): 
    list_display = ['name' , 'price']
    search_fields = ['name', 'description' ]
    list_filter = ('category', 'people')

admin.site.register(Menu , MenusAdmin)
admin.site.register(Category)