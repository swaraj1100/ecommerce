from django.contrib import admin
from .models import category,Product


class  categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,categoryadmin)



class productAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20

admin.site.register(Product,productAdmin)


# class  productadmin(admin.ModelAdmin):
#     list_display = ['name','price','stock','available','created''updated']
#     list_editable = ['price','stock','available']
#     prepopulated_fields = {'slug':('name',)}
#     list_per_page = 20
# admin.site.register(product,productadmin)