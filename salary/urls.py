from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Simple login for securing site on Heroku
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),

    # Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', admin.site.urls),

    # Project URLs go here

	url(r'^employee/(?P<employee_id>\d+)/$', 'apps.salaries.views.employee', name = 'employee'),
	url(r'^college/(?P<college_id>\d+)/$', 'apps.salaries.views.college', name = 'college')


)

urlpatterns += staticfiles_urlpatterns()
