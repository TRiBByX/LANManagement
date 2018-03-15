from django.conf.urls import url
from django.contrib import admin
from dashboard.views import Index

urlpatterns = [
    url(r'^$', Index.as_view(), name='Dashboard'),
]
