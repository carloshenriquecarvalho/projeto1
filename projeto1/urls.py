from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def my_view(request):
    return HttpResponse('Carlos é o brabo')

urlpatterns = [
    path('sobre/', my_view),
    path('admin/', admin.site.urls)
]
