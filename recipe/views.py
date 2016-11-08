# from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Recipe


def recipe_list(request):

    recipe_list = Recipe.objects.all()
    return render_to_response('recipe/recipe_list.html', {'recipe_list': recipe_list})

