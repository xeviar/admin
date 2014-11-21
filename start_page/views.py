from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from conf import taskconf
import sys
#import testdata
from start_page.models import *
import json

_dict = {}
_model = model_data()

def init(request):
	_dict["user"]          = request.user
	#_dict["product"]       = taskconf.TASKITEM
	_dict["product"]       = _model.getAllProduct()
	#_dict["list"]          = taskconf.TASKLIST
	_dict["list"]          = _model.getAllProductItem()
	_dict["selected_product"] = "IM"

def login_error(request):
	return HttpResponse('Unauthorized User, Please contact System Admin!!!', status=401)

@login_required
def start_page(request):
	init(request)
	return render_to_response('start_page/start_page.html', _dict)

def test(request, var1=""):
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


@login_required
def getdetail(request, v_product, v_item):
	try:
		ret = {'data': []}
		_retlist = []
		_prod = Product_tbl.objects.get(product_name=v_product)
		_proditem = Product_item_tbl.objects.filter(product=_prod.id).filter(item_name=v_item)
		_set = Item_log_tbl.objects.filter(item=_proditem[0].id)

		for v in _set:
			_retlist.append(v.tojson())

		ret['data'] = _retlist
		print json.dumps(ret)
		return HttpResponse(json.dumps(ret))
	except:
		print "Unexpected error:", sys.exc_info()[0]
		return HttpResponse("1")

def log_out(request):
    logout(request)
    return HttpResponse('succeed!')
