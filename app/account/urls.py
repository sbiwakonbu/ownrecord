from django.conf.urls import url, include
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/$', login,
        {'template_name': 'login/index.jinja'}),
    url(r'^logout/$', logout,
        {'template_name': 'logout/index.jinja'}),
]
