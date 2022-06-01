from rest_framework import viewsets
from .models import Recipe, RecipeStep, Ingredient
from .serializers import RecipeSerializer, RecipeStepSerializer, IngredientSerializer


class RecipeView(viewsets.ReadOnlyModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer