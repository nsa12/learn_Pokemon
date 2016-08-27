from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PokemonGo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'search.views.index', name='newIndex'),
    url(r'^pokemon$', 'search.views.index', name='index'),
    #url(r'^random$', 'search.views.random', name='random'),
    url(r'^searchGET$', 'search.views.searchget', name='searchGET'),
    url(r'^searchPOST$', 'search.views.searchpost', name='searchPOST'),
    #url(r'^search/(\d+)$', 'search.views.search2', name='search2'),		#unnamed grouping
    #url(r'^search/(?P<foo>\d+)', 'search.views.search2', name='search2'),  #named grouping
    #url(r'^pokedex$', 'search.views.newIndex', name='newIndex'),
    url(r'^searchREDIRECT/(?P<search_string>[\*\w\-]+)/$', 'search.views.searchredirect', name='searchredirect'),
    url(r'^searchLISTJS$', 'search.views.searchlistjs', name='searchLISTJS'),
    url(r'^edit/(\d+)', 'search.views.edit', name="edit"),
    url(r'^p/(?P<page_id>\d+)', 'search.views.index2', name='index2'),
    url(r'^pokemon/(?P<pokemon_id>\d+)/(?P<pokemon_name>[\w\-]+)', 'search.views.description', name='description'),
    url(r'^pokemon/(?P<pokemon_id>\d+)/', 'search.views.short_url', name='short_url'),
)