from django.conf.urls import url, include
from account.views import login, logout_view

urlpatterns = [
    url(r'^login/$', login,
        {'template_name': 'login/index.jinja'}),
    url(r'^logout/$', logout_view),
]
