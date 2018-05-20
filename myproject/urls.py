from django.conf.urls import patterns, include, url
from django.contrib import admin
from museos import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.pag_principal, name='Inicio'),
    url(r'^museos$', views.pag_museos, name='Todos los museos'),
    url(r'^about$', views.about, name="About"),
    url(r'^museos/(\d+)$', views.pag_museo, name='Pagina de cada museo'),
    url(r'^logout$', views.logoutUser),
    url(r'^login$', views.loginUser),
    url(r'^xml$', views.xml_main, name="XML de Main"),
    url(r'^json$', views.json_main, name="JSON de Main"),
    url(r'^rss$', views.rss_comentarios, name="RSS de comentarios"),
    url(r'^(.+)/xml', views.xml_usuario, name="XML de usuario"),
    url(r'^(.+)/json', views.json_usuario, name="JSON de usuario"),
    url(r'^(.+)', views.pag_user, name="Pagina personal del usuario"),
]
