from django.contrib import admin
from .models import Customer,Product,Order

# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    list_display=['first_name','last_name','mobile','email','location']
admin.site.register(Customer,AdminCustomer)

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','description','created_date','category']
admin.site.register(Product,AdminProduct)

class AdminOrder(admin.ModelAdmin):
    list_display=['status','created_date']
admin.site.register(Order,AdminOrder)
