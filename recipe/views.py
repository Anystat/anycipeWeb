from django.shortcuts import render_to_response

import requests
import re

SITE_ROOT = 'http://85.143.221.95:8080'


def recipe_list(request):
    r = Request()
    args = {}
    args['recipe_list'] = r.get_recipe_list()
    args['query'] = request.GET.get('query')

    if args['query']:
        args['recipe_list'] = r.get_recipe_with_ingr(args['query'])
    return render_to_response('recipe/recipe_list.html', args)


def recipe_detail(request, name):
    r = Request()
    args = {}
    args['recipe'] = r.get_recipe(name)
    return render_to_response('recipe/recipe_detail.html', args)


def ingridients_list(request):
    r = Request()
    args = {}
    args['ingridients_list'] = r.get_ingridients_list()
    args['query'] = request.GET.get('query')

    if args['query']:
        args['recipe_list'] = r.get_recipe_with_ingr(args['query'])
        return render_to_response('recipe/recipe_list.html', args)
    return render_to_response('recipe/ingridients_list.html', args)


def ingridients_detail(request, name):
    r = Request()
    args = {}
    args['ingridient'] = r.get_inrg(name)
    return render_to_response('recipe/ingridients_detail.html', args)


class Request:
    # send request to REST and return json response

    def __init__(self):
        self.root = SITE_ROOT

    def get_ingridients_list(self):
        # Список продуктов
        request = '/ingredients'
        url = self.root + request
        response = requests.get(url)

        return response.json()

    def get_recipe_list(self):
        # Список блюд
        request = '/receipts'
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


    def get_recipe_with_ingr(self, query):
        query = re.compile(r"\w+").findall(query)
        ingr = ''
        for q in query:
            ingr = ingr + q + ','
        request = '/receipts/find?ingredient[]=' + ingr[:-1]
        url = self.root + request
        response = requests.get(url)

        return response.json()
