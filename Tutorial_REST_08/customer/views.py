from django.shortcuts import render
from .models import Customer
from rest_framework import generics
from .serializers import CustomerSerializer

class CustomerCreate(generics.CreateAPIView):
  queryset = Customer.objects.all(),
  serializer_class = CustomerSerializer

class CustomerList(generics.ListAPIView):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveAPIView):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer

class CustomerUpdate(generics.RetrieveUpdateAPIView):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer

class CustomerDelete(generics.RetrieveDestroyAPIView):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer