from time import strptime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from datetime import datetime
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.template import loader

from .utils import Calendar


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def course_calendar(request, year=datetime.today().year, month=datetime.today().strftime("%B")):
    if request.path == '/courses':
        return HttpResponseRedirect(f'/courses/{year}/{month}/')

    # Instantiate our calendar class with today's year and date
    cal = Calendar(year, strptime(month, '%B').tm_mon)

    # Call the formatmonth method, which returns our calendar as a table
    cal_data = cal.get_month()
    context = {
        'calendar': cal_data['calendar'],
        'month': month,
        'prev': cal_data['prev'],
        'next': cal_data['next']
    }
    
    html_template = loader.get_template('courses/course_list.html')
    return HttpResponse(html_template.render(context, request))
