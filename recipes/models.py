from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.FloatField()
    unit = models.CharField(max_length=200)


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipe_steps', on_delete=models.CASCADE)
    step_number = models.IntegerField(default=0)
    contents = models.TextField()
