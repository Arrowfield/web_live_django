
from django.conf.urls import url

from django.contrib import admin

from . import view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',view.main),
    url(r'^login/',view.login)
]
