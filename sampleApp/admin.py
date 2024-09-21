from django.contrib import admin

from sampleApp.models import ProductTable, ShopTable

# Register your models here.

admin.site.register(ShopTable)
admin.site.register(ProductTable)


