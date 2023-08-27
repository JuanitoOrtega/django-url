from django.urls import path

from .views import short_redirect_view, ShortCBView


urlpatterns = [
    path('view-1/', short_redirect_view),
    path('view-2/', ShortCBView.as_view()),
]