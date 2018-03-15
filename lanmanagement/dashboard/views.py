# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.

class Index(View):
    
    def get(self, request):
        return HttpResponse(200)
