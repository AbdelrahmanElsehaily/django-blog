from django.shortcuts import render
from  django.http import HttpResponse
from django.template import context
from django.template.loader import get_template
# Create your views here.
from .models import Post
def post_list(request):

    return  render(request,'blog\post_list.html',{})

