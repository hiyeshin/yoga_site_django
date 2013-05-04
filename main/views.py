from django.http import HttpResponse
from django.template import Context, loader
from models import *
import json

def main(request):
    t = loader.get_template('main.html')
    c = Context({
    })
    return HttpResponse(t.render(c))
