from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, IngredientSerializer
from .models import Category, Ingredient

# Create your views here.
# viewsets base class provides implementation for CRUD operations by default
class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class IngredientView(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

