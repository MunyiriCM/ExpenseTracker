from rest_framework import serializers
from .models import Category, Expense


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # nested representation
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )

    class Meta:
        model = Expense
        fields = ["id", "category", "category_id", "amount", "description", "date"]


#CategorySerializer → converts Category objects to/from JSON.
#
#ExpenseSerializer →

#Shows category details (nested serializer).

#Allows setting category by ID when creating (category_id).

#Returns amount, description, date.