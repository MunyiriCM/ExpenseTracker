from django.shortcuts import render
from django.http import HttpResponse
#for permissions
from rest_framework import generics, permissions
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
    permission_classes = [permissions.IsAuthenticated]  # must be logged in to create

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # attach logged-in user as owner


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
