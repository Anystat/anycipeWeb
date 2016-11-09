# from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Recipe


def recipe_list(request):

    recipe_list = Recipe.objects.all().order_by('-create_date')

    query = request.GET.get('query')

    if query:
        recipe_list = recipe_list.filter(text__icontains=query)

    return render_to_response('recipe/recipe_list.html', {'recipe_list': recipe_list, 'query': query})


def recipe_detail(request, id):

    recipe = Recipe.objects.get(id=id)

    return render_to_response('recipe/recipe_detail.html', {'recipe_detail': recipe})
