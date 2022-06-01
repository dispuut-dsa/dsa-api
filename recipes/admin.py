from django.contrib import admin

from .models import Recipe, Ingredient, RecipeStep

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'description', 'ingredients', 'recipe_steps')
 
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'name', 'quantity', 'unit')

class RecipeStepAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'step_number', 'contents')
    
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeStep, RecipeStepAdmin)
