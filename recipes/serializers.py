from rest_framework import serializers
from .models import Recipe, Ingredient, RecipeStep


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity', 'unit')


class RecipeStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ['contents']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    recipe_steps = RecipeStepSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'author', 'description', 'ingredients', 'recipe_steps')
