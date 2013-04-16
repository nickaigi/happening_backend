# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from core.models import News, Tag 

def home(request):
    """
    Home page for the happening app
    """
    news = News.objects.filter(is_active=True)
    return render_to_response('home.html', {'news': news}, context_instance=RequestContext(request))
