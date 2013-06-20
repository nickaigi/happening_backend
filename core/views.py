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


def news_view(request,news_id):
    """
    The news display page
    """
    news = News.objects.get(id=news_id)
    return render_to_response('news.html',{'news': news
        }, context_instance=RequestContext(request))
