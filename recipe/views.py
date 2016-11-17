from django.shortcuts import render_to_response
from .models import Recipe

import requests
# JSON = open('receipts.json', 'r')
JSON = {
  "receipt": "борщ",
  "ingredients": [
    {
      "name": "томат",
      "amount": 100,
      "unit": "грамм"
    },
    {
      "name": "чеснок",
      "amount": "",
      "unit": ""
    }
  ],
  "persons": 2,
  "energy": {
    "calorific value": 250,
    "protein": 10,
    "fat": 5,
    "carbohydrates": 10
  },
  "description": "Hello World",
  "image": {
    "_id": "",
    "chunkSize": "",
    "uploadDate": "",
    "length": "",
    "md5": "",
    "filename": ""
  }
}

SITE_ROOT = ''


def recipe_list(request):

    args = {}
    args['recipe_list'] = Recipe.objects.all().order_by('-create_date')
    args['query'] = request.GET.get('query')

    if args['query']:
        args['recipe_list'] = args['recipe_list'].filter(text__icontains=args['query'])
    print(args)
    return render_to_response('recipe/recipe_list.html', args)


def recipe_detail(request, id):
    args = {}
    # args['recipe'] = Recipe.objects.get(id=id)
    args['recipe'] = JSON

    # return render_to_response('recipe/recipe_detail.html', args)
    return render_to_response('recipe/recipe_detail_JSON.html', args)
    # return JsonResponse(JSON, safe=False)


class Request:
    # send request to REST and return json response

    def __init__(self):
        self.root = SITE_ROOT

    def get_products_list(self):
        # Список продуктов
        request = '/sites'
        url = self.root + request
        response = requests.get(url)

        # return response.json()
        return JSON
