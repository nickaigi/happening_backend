# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    """
    Home page for the happening app
    """
    return render_to_response('home.html', {}, context_instance=RequestContext(request))
