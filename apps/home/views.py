# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse

from .models import Course
from .forms import CourseForm, CourseSignUpForm


def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

    
def home_templates(request):
    return request_template(request, 'home')


def info_templates(request):
    return request_template(request, 'info')


@login_required(redirect_field_name='next', login_url="/login/")
def template_templates(request):
    return request_template(request, 'templates')


def request_template(request, directory, context={}):
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        try:
            html_template = loader.get_template(f'{directory}/{load_template}.html')
        except:
            try:
                html_template = loader.get_template(f'{directory}/{load_template}')
            except:
                html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(redirect_field_name='next', login_url="/login/")
def course_list(request):
    course_list = Course.objects.all()
    context = {
        'course_list': course_list
    }
    html_template = loader.get_template('courses/course_list.html')
    return HttpResponse(html_template.render(context, request))


@login_required(redirect_field_name='next', login_url="/login/")
def course_sign_up(request, course_id):
    submitted = False
    try:
        searched_course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return HttpResponseRedirect('/courses')
    form = CourseSignUpForm(request.POST or None, instance=searched_course)
    if request.method == "POST":
        if form.is_valid():
            if not request.user.is_authenticated:
                return redirect(f'/courses/view/{course_id}/')
        return HttpResponseRedirect('/courses')
    else:
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'course': searched_course,
        'form': form
    }
    html_template = loader.get_template(f'courses/course_signup.html')
    return HttpResponse(html_template.render(context, request))


@staff_member_required
def add_course(request):
    submitted = False
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/courses/add?submitted=True')
    else:
        form = CourseForm
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form': form,
        'submitted': submitted
    }
    html_template = loader.get_template('courses/add_course.html')
    return HttpResponse(html_template.render(context, request))


@staff_member_required
def edit_course(request):
    searched_course = Course.objects.all()
    context = {
        'course_list': searched_course
    }
    html_template = loader.get_template('courses/course_edit.html')
    return HttpResponse(html_template.render(context, request))


def course_view(request, course_id):
    if request.POST:
        return HttpResponseRedirect(f'/courses/signup/{course_id}/')
    try:
        searched_course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return HttpResponseRedirect('/courses')
    context = {
        'course': searched_course
    }
    html_template = loader.get_template('courses/course_view_id.html')
    return HttpResponse(html_template.render(context, request))
    
    
@staff_member_required
def edit_course_id(request, course_id):
    try:
        searched_course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return HttpResponseRedirect('/courses/edit')
    form = CourseForm(request.POST or None, instance=searched_course)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/courses/edit')
    context = {
        'course': searched_course,
        'form': form
    }
    html_template = loader.get_template('courses/course_edit_id.html')
    return HttpResponse(html_template.render(context, request))


@staff_member_required
def delete_course_id(request, course_id):
    try:
        searched_course = Course.objects.get(pk=course_id)
        searched_course.delete()
    except Course.DoesNotExist:
        pass
    return HttpResponseRedirect('/courses/edit')
