# Create your views here.

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404,render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

#@login_required
def start_page(request):

    return render_to_response('start_page/start_page.html')
#    return HttpResponse("hello")
