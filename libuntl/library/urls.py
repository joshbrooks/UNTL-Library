from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^$', views.ResourceList.as_view())
]