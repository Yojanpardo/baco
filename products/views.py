from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product

# Create your views here.

def home(request):
	product = Product.objects.order_by('id')
	template = loader.get_template('home.html')
	context = {
		'product':product
	}
	return HttpResponse(template.render(context, request))