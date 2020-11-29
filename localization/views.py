from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils.translation import gettext as _


def index(request):
    text = _('Hello from views')
    return render(request, 'index.html', context={'text': text})
