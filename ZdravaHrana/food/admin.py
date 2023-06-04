from typing import Any, Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import *
# Register your models here.
 
# забелешка дека продуктите може да се додаваат и во делот за категории. 
# Притоа, во рамки на Админ панелот потребно INLINE
#- При креирањето на продуктот, корисникот се доделува автоматски 
# според најавениот корисник
#- Откако еден продукт ќе биде дефиниран и зачуван, истиот може да се 
# промени само од корисникот кој го креирал продуктот
#- Не е дозволено бришење на категориите доколку корисникот не е супер корисник
#- За клиентите и категориите во листата се прикажуваат само нивните имиња (и
#презиме за клиентот)

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name']
    def has_add_permission(self, request: HttpRequest) -> bool:
        return super().has_add_permission(request)
    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return super().has_change_permission(request, obj)
    def has_view_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return super().has_view_permission(request, obj)
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return super().has_delete_permission(request, obj)

class ProductAdmin(admin.ModelAdmin):
    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        if request.user.is_superuser or obj.user==request.user:
            return True
        return False
    def has_add_permission(self, request: HttpRequest) -> bool:
        return True
    
    def has_view_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return super().has_view_permission(request, obj)
    
    exclude = ['user']
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        if obj:
            obj.user = Client.objects.get(user=request.user)
        super().save_model(request,obj,form,change)
    
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        if request.user.is_superuser or obj.user==request.user:
            return True
        return False

class ProductCategoryAdmin(admin.TabularInline):
    model = Product
    extra = 0  

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ProductCategoryAdmin]
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        if request.user.is_superuser:
            return True
        return False
    
    def has_add_permission(self, request: HttpRequest) -> bool:
        return super().has_add_permission(request)
    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return super().has_change_permission(request, obj)
    def has_view_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return super().has_view_permission(request, obj)

class SaleAdmin(admin.ModelAdmin):
    list_display = ['product', 'client']
    list_filter = ['client', 'product']
    def has_add_permission(self, request: HttpRequest) -> bool:
        return super().has_add_permission(request)
    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return super().has_change_permission(request, obj)
    def has_view_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return super().has_view_permission(request, obj)
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return super().has_delete_permission(request, obj)

class ProductsInSaleAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        return super().has_add_permission(request)
    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return super().has_change_permission(request, obj)
    def has_view_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return super().has_view_permission(request, obj)
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return super().has_delete_permission(request, obj)


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(ProductsInSale, ProductsInSaleAdmin)



