from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404,render_to_response
from django.contrib.auth.decorators import login_required
from conf import taskconf
import sys
import testdata
from start_page.models import *

_dict = {}
_model = model_data()

def init(request):
	_dict["user"]          = request.user
	#_dict["product"]       = taskconf.TASKITEM
	_dict["product"]       = _model.getAllProduct()
	#_dict["list"]          = taskconf.TASKLIST
	_dict["list"]          = _model.getAllProductItem()
	_dict["selected_product"] = "IM"

@login_required
def start_page(request):
	init(request)
	return render_to_response('start_page/start_page.html', _dict)

def test(request, var1=""):
#    return HttpResponse("hello")
	return render_to_response('start_page/test.html', {"blood": var1})


@login_required
def product(request, product):
	init(request)
	_dict["selected_product"] = product
	return render_to_response('start_page/start_page.html', _dict)

@login_required
def getstatus(request, v_product, v_item):
	try:
		_prod = Product_tbl.objects.get(product_name=v_product)
		_proditem = Product_item_tbl.objects.filter(product=_prod.id).filter(item_name=v_item)
		v = _proditem[0].item_status
		#v = testdata.testdata[v_product][v_item]
		return HttpResponse(v)
	except:
		print "Unexpected error:", sys.exc_info()[0]
		return HttpResponse("1")