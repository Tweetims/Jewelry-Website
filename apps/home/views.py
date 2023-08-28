# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import apps.home.config
from django import template
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
from apps.authentication.decorators import allowed_users

from .models import CourseSignUp, Design
from .forms import CourseSignUpForm, WebsiteUserForm
from django.db.models.query_utils import Q


def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

    
def home_templates(request):
    return request_template(request, 'home')


def info_templates(request):
    return request_template(request, 'info')


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
        if request.path.startswith('/media'):
            return
        else:
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
def course_sign_up(request, uuid):
    design = Design.objects.get(uuid=uuid)
    sign_up = CourseSignUp(account=request.user.websiteuser, design=design)
    form = CourseSignUpForm(request.POST or None, instance=sign_up)
    if request.method == "POST":
        if form.is_valid():
            if not request.user.is_authenticated:
                return redirect('/')
            form.save()
            return redirect('/')
        else:
            pass
    context = {
        'design': design,
        'form': form,
        'metal_prices': apps.home.config.MyConfig.METAL_PRICES,
        'melee_prices': apps.home.config.MyConfig.MELEE_PRICES,
    }
    html_template = loader.get_template(f'courses/course_signup.html')
    return HttpResponse(html_template.render(context, request))


def design_search(request):
    context = {
        'metal_prices': apps.home.config.MyConfig.METAL_PRICES,
        'melee_prices': apps.home.config.MyConfig.MELEE_PRICES,
    }
    if request.method == "POST":
        searched = request.POST['searched']
        results = Design.objects.filter(Q(name__contains=searched) | Q(tags__name__contains=searched)).distinct()
        context['searched'] = searched
        context['designs'] = results
    else:
        results = Design.objects.order_by('?')[:10]
        context['designs'] = results
    html_template = loader.get_template(f'courses/design_search.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer', 'admin'])
def user_page(request):
    form = WebsiteUserForm(instance=request.user.websiteuser)
    context = {
        'form': form
    }
    html_template = loader.get_template('accounts/user.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user_settings(request):
    form = WebsiteUserForm(request.POST or None, instance=request.user.websiteuser)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/account')
    context = {
        'form': form
    }
    html_template = loader.get_template('accounts/user_settings.html')
    return HttpResponse(html_template.render(context, request))

