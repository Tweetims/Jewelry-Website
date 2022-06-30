from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from datetime import datetime
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from django.template import loader

from apps.home.models import Event
from .utils import Calendar
import calendar
from calendar import HTMLCalendar


def get_date(req_day):
        if req_day:
            year, month = (int(x) for x in req_day.split('-'))
            return date(year, month, day=1)
        return datetime.today()

def event_calendar(request, year=datetime.today().year, month=datetime.today().strftime("%B")):
    # use today's date for the calendar
    d = get_date(request.GET.get('day', None))

    # Instantiate our calendar class with today's year and date
    cal = Calendar(d.year, d.month)

    # Call the formatmonth method, which returns our calendar as a table
    html_cal = cal.formatmonth(withyear=True)
    context = {
        'calendar': mark_safe(html_cal)
    }
    
    html_template = loader.get_template('events/event_list.html')
    return HttpResponse(html_template.render(context, request))
