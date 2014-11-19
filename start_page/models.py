from django.db import models


STATUS = (
	('1', 'OK'),
	('2', 'WARNING'),
	('3', 'CRITICAL'),
)

class Product_tbl(models.Model):
	product_name = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.product_name

class Product_item_tbl(models.Model):
	product = models.ForeignKey(Product_tbl)
	item_name = models.CharField(max_length=50)


	item_status = models.CharField(max_length=1, choices=STATUS, default='1')
	item_description = models.TextField()
	update_timstamp = models.IntegerField()
	def __unicode__(self):
		return "cccc"

class Item_log_tbl(models.Model):
	item = models.ForeignKey(Product_item_tbl)

	item_status = models.CharField(max_length=1, choices=STATUS, default='1')
	item_description = models.TextField()
	update_timstamp = models.IntegerField()
	def tojson(self):
		return '{"status":"%s","desc":"%s","timestamp":%d}' % (_getValue(self.item_status), self.item_description, self.update_timstamp)


def _getValue(q):
    for choice in STATUS:
        if choice[0] == q:
            return choice[1]
    return ''

class model_data:
	_productlist = []
	_productdict = {}

	def __init__(self):
		pass

	def getAllProduct(self):
		#if self._productlist:
		#	return self._productlist
		
		self._productlist = []
		for i in Product_tbl.objects.all():
			self._productlist.append(i.product_name)

		return self._productlist

	def getAllProductItem(self):
		#if self._productdict:
		#	return self._productdict
		self._productdict = {}
		for i in Product_tbl.objects.all():
			_list = []
			for item in Product_item_tbl.objects.filter(product=i.id):
				_list.append(item.item_name)

			self._productdict[i.product_name] = _list

		return self._productdict