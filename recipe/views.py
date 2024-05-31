from django.shortcuts import render, get_object_or_404
from .models import Recipe
import datetime

def main(request):
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 12, 31, 23, 59, 59)
    recipes = Recipe.objects.filter(created_at__range=(start_date, end_date))
    return render(request, 'main.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})