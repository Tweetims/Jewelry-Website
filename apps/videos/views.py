from django.http import HttpResponse
from django.template import loader
from .models import Video

def index(request):
    videos = Video.objects.all()
    context = {
        'videos': videos,
    }

    html_template = loader.get_template('videos/video_page.html')
    return HttpResponse(html_template.render(context, request))
