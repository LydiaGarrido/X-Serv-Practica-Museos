from django.conf.urls import patterns, include, url
from django.contrib import admin
from museos import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.pag_principal, name='Inicio'),
    url(r'^museos$', views.pag_museos, name='Todos los museos'),
]
