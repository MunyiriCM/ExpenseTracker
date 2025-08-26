from django.shortcuts import render
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
#for permissions
from rest_framework import generics, permissions, filters
from .models import Expense
from .serializers import ExpenseSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
def home(request):
    return HttpResponse("Welcome to Xtracker 🚀")


# for permissions
class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    # ✅ Add filters & search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'date', 'amount']   # filter by exact match
    search_fields = ['description', 'category']         # search text fields
    ordering_fields = ['date', 'amount']                # order by date or amount
    ordering = ['-date']                                # default ordering (newest first)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
