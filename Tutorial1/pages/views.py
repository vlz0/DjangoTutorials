from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
'''
    def homePageView(request):
        return HttpResponse('Hello World!')
'''
class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Daniel Vélez",
        })
        
        return context
    
class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price": 2600000},
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 5000000},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 2000000},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 150000}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] =  "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)
    
class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        viewData = {}
        try:
            product = Product.products[int(id) - 1]
        except(IndexError, ValueError):
            return HttpResponseRedirect(reverse('home'))
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData) 