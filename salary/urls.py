from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from haystack.views import SearchView, search_view_factory

admin.autodiscover()

#API
from tastypie.api import Api
from apps.salaries.api import CollegeResource

v1_api = Api(api_name='v1')
v1_api.register(CollegeResource())

urlpatterns = patterns('',
    
    # Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', admin.site.urls),

    #haystax
    (r'^search/', include('haystack.urls')),
    url(r'^search/autocomplete/$', 'apps.salaries.views.autocomplete'),
    # Project URLs go here

    (r'^api/', include(v1_api.urls)),
    url(r'^landing/', 'apps.salaries.views.landing',name = 'landing'),
	url(r'^employee/(?P<employeeSuper_id>\d+)/$', 'apps.salaries.views.employeeSuper', name = 'employee'),
	url(r'^college/(?P<college_id>\d+)/$', 'apps.salaries.views.college', name = 'college'),
	url(r'^department/(?P<department_id>\d+)/$', 'apps.salaries.views.department', name = 'department'),
	url(r'^position/(?P<position_id>\d+)/$', 'apps.salaries.views.position', name = 'position'),
    url(r'^campus/(?P<campus_id>\d+)/$', 'apps.salaries.views.campus', name = 'campus'),
	url(r'^bubbles/', 'apps.salaries.views.bubbles', name = 'bubbles'),
    url(r'^deans/', 'apps.salaries.views.deans', name = 'deans'),

#    url(r'^/search/autocomplete/', 'apps.salaries.views.autocomplete')


)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

