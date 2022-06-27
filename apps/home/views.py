# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime
from django import template
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

import calendar
from calendar import HTMLCalendar
from .models import Event
from .forms import EventForm

# videos app models
from apps.videos.models import Video


def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
    
def about(request):
    context = {}
    html_template = loader.get_template('home/about-us.html')
    return HttpResponse(html_template.render(context, request))

def contact(request):
    context = {}
    html_template = loader.get_template('home/contact-us.html')
    return HttpResponse(html_template.render(context, request))
    
@login_required(login_url="/login/")
def events(request, year=datetime.today().year, month=datetime.today().strftime("%B")):
    # convert month from name to number
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    # create calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month_number
    )
    context = {
        "year": year,
        "month": month,
        "month_number": month_number,
        "calendar": cal,
    }
    html_template = loader.get_template('events/events.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def event_list(request):
    event_list = Event.objects.all()
    context = {
        'event_list': event_list
    }
    html_template = loader.get_template('events/event_list.html')
    return HttpResponse(html_template.render(context, request))


@staff_member_required
def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    videos = Video.objects.filter(title__contains='119')
    context = {
        'form': form,
        'submitted': submitted,
        'videos': videos
    }
    html_template = loader.get_template('events/add_event.html')
    return HttpResponse(html_template.render(context, request))
    
