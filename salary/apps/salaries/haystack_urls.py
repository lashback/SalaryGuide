from haystack.views import SearchView
from haystack.query import SearchQuerySet
from django.conf.urls.defaults import patterns, url

sqs = SearchQuerySet() 

urlpatterns = patterns('haystack.views',
    url(r'^&', SearchView(load_all=False,searchqueryset=sqs),name='haystack_search'), 
)
