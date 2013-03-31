# Create your views here.
from django.shortcuts import render_to_response
from blog.models import Posts

def home(request):
  entries = Posts.objects.all()[:10]
  return render_to_response('blog/index.html', {'posts':entries})
