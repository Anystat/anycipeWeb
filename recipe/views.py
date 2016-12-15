from django.shortcuts import render_to_response, render
from django.template.context_processors import csrf
from django.core.urlresolvers import resolve, Resolver404
import requests
import re
from django import template

register = template.Library()

# SITE_ROOT = 'http://85.143.221.95:8080'
SITE_ROOT = 'http://008080.ha2s4mjugmxdemrrfy4tk.nblz.ru/'


def recipe_list(request):
    r = Request()
    args = {}
    args['recipe_list'] = r.get_recipe_list()
    args['query'] = request.GET.get('query')

    if args['query']:
        args['recipe_list'] = r.get_recipe_with_ingr(args['query'])

    return render(request, 'recipe/recipe_list.html', args)


def recipe_detail(request, name):
    r = Request()
    args = {}
    args['recipe'] = r.get_recipe(name)

    return render(request, 'recipe/recipe_detail.html', args)


def ingredients_list(request):
    r = Request()
    args = {}
    args['ingredients_list'] = r.get_ingredients_list()
    args['query'] = request.GET.get('query')
    args['checks'] = request.POST.getlist('checks')

    args.update(csrf(request))
    if request.method == 'POST':
        args['recipe_list'] = r.get_recipe_with_check(args['checks'])

        return render(request, 'recipe/recipe_list.html', args)

    if args['query']:
        args['recipe_list'] = r.get_recipe_with_ingr(args['query'])

        return render(request, 'recipe/recipe_list.html', args)

    return render(request, 'recipe/ingredients_list.html', args)


def ingredients_detail(request, name):
    r = Request()
    args = {}
    args['ingredient'] = r.get_inrg(name)

    return render(request, 'recipe/ingredients_detail.html', args)


class Request:
    # send request to REST and return json response

    def __init__(self):
        self.root = SITE_ROOT

    def get_ingredients_list(self):
        # Список продуктов
        request = '/ingredients'
        url = self.root + request
        response = requests.get(url)

        return response.json()

    def get_recipe_list(self):
        # Список блюд
        # request = '/receipts'
        request = '/receipts/page/1?size=10'
        url = self.root + request
        response = requests.get(url)

        return response.json()

    def get_recipe(self, name):
        request = '/receipts/' + name
        url = self.root + request
        response = requests.get(url)

        return response.json()[0]

    def get_inrg(self, name):
        request = '/ingredients/' + name
        url = self.root + request
        response = requests.get(url)

        return response.json()[0]

    def get_ingr_name_from_id(self, id):
        return self.get_ingredients_list()[id].get('ingredient')


    def get_recipe_with_check(self, checks):
        ingr = ''
        for i in range(len(checks)):
            ingr = ingr + self.get_ingr_name_from_id(int(checks[i])-1) + ','
        request = '/receipts/find?ingredient[]=' + ingr[:-1]
        print(request)
        url = self.root + request
        response = requests.get(url)

        return response.json()

    def get_recipe_with_ingr(self, query):
        print(query)
        query = re.compile(r"\w+").findall(query)
        ingr = ''
        for q in query:
            ingr = ingr + q + ','
        request = '/receipts/find?ingredient[]=' + ingr[:-1]
        url = self.root + request
        response = requests.get(url)

        return response.json()
