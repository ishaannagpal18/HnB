from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
import uuid
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import *
from django.core.mail import send_mail
from django.views import View


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def shop(request):
    return render(request, 'shop.html')

def product_detail(request):
    return render(request, 'product_detail.html')

def portfolio_single(request):
    return render(request, 'portfolio_single.html')