from django.conf.urls import url
from recipe.views import *

urlpatterns = [
    url(r'^$', recipe_list, name='recipe_list'),
    url(r'^recipe/(?P<id>\d+)/$', recipe_detail, name='recipe_detail'),
]