from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class StoreAdmin(admin.ModelAdmin):
    list_display=['id','product_name','price','stock','category','modified_date']
    prepopulated_fields={'slug':('product_name',)}
