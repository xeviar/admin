from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404,render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def start_page(request):
	print request
	userid = request.user
	return render_to_response('start_page/start_page.html', {"user": userid})

def test(request, var1=""):
#    return HttpResponse("hello")
	return render_to_response('start_page/test.html', {"blood": var1})