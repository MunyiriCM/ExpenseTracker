from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Expense, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "amount", "date")
    list_filter = ("category", "date", "user")
    search_fields = ("description",)


#👉 This lets you manage categories and expenses in Django Admin.