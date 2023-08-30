from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import ShortURL


# Create your views here.
def short_redirect_view(request, shortcode=None, *args, **kwargs): # function based view FBV
    obj = get_object_or_404(ShortURL, shortcode=shortcode)
    return HttpResponse('Hello {sc}'.format(sc=obj.url))


class ShortCBView(View): # class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        return HttpResponse('Hello again {sc}'.format(sc=shortcode))

    def post(self, request, *args, **kwargs):
        return HttpResponse()


'''
def short_redirect_view(request, shortcode=None, *args, **kwargs): # function based view FBV
    # print(request.user)
    # print(request.user.is_authenticated())
    print('method is \n')
    print(request.method)
    # obj = ShortURL.objects.get(shortcode=shortcode)

    obj = get_object_or_404(ShortURL, shortcode=shortcode)
    # obj_url = obj.url

    # try:
    #     obj = ShortURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = ShortURL.objects.all().first()

    # obj_url = None
    # qs = ShortURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url

    return HttpResponse('Hello {sc}'.format(sc=obj.url))
'''