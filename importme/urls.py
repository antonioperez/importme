from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'importme.views.Home', name='home'),
    url(r'^login/$', 'importme.views.Login', name='login'),
    url(r'^logout/$', 'importme.views.Logout', name='logout'),
    url(r'^blog/', include('blog.urls')),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
