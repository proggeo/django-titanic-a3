from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^trees$', hello.views.googlemapstrees, name='trees'),
    url(r'^cars$', hello.views.cars, name='cars'),
    url(r'^carsandtrees$', hello.views.carsandtrees, name='carsandtrees'),
    url(r'^houses$', hello.views.houses, name='houses'),
    url(r'^dataset$', hello.views.titanic_json, name='dataset'),
    url(r'^trees_json$', hello.views.trees_json, name='trees_json'),
    url(r'^cars_json$', hello.views.cars_json, name='cars_json'),
    url(r'^houses_json$', hello.views.houses_json, name='houses_json'),
    url(r'^admin/', include(admin.site.urls)),
]
