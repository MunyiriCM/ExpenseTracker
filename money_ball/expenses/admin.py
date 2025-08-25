from django.contrib import admin
from .models import Category, Expense

# Register your models here.

#admin.site.register(Category)
#admin.site.register(Expense)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")              # shows these columns in the list view
    search_fields = ("name",)                  # adds search box
    ordering = ("name",)                       # order by name


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "amount", "description", "date")  # columns shown
    list_filter = ("category", "date")         # filters on sidebar
    search_fields = ("description",)           # search box for descriptions
    date_hierarchy = "date"                    # date navigation at top
    ordering = ("-date",)                      # newest first

##Step 2: What This Does in Admin

#    CategoryAdmin

#   You can search categories by name.

#  Sorted alphabetically.
#   Columns shown: ID and name.

#   ExpenseAdmin

#   Shows ID, category, amount, description, date.

#   Filter by category or date.

#   Search expenses by description.

#   Date hierarchy at top (click months/years).

#   Ordered with newest expense first.