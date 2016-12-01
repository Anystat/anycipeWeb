from django.conf.urls import url
from recipe.views import *

app_name = 'recipe'
urlpatterns = [
    url(r'^$', recipe_list, name='recipe_list'),
    url(r'^recipe/(?P<name>.+)/$', recipe_detail, name='recipe_detail'),
    url(r'^ingridients/$', ingridients_list, name='ingridients_list'),
]