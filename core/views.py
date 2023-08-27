from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
def short_redirect_view(request, *args, **kwargs): # function based view FBV
    return HttpResponse('Hello')


class ShortCBView(View): # class based view
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello again')