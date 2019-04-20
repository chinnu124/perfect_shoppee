from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def searchResult(request):
	products=None
	query=None
	if q in request.GET:
		query=request.GET.get('q')
		products=product.objects.all().filter(Q(name_contains=query)|Q(description_contains=query))
	return render(request,'search.html',{'query':query, 'products':products}) 
