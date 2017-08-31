from django.contrib import admin

# Register your models here.

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
	list_display = ('name', 'category', 'price')
	list_filter = ('category')