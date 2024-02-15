from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

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
        except IndexError:
            return HttpResponseRedirect(reverse('home'))
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData) 

class ProductForm(forms.Form): 
    name = forms.CharField(required=True) 
    price = forms.FloatField(required=True)
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("El precio debe ser mayor a cero.")
        return price
    
class ProductCreateView(View): 
    template_name = 'products/create.html' 
    
    def get(self, request): 
        form = ProductForm() 
        viewData = {} 
        viewData["title"] = "Create product" 
        viewData["form"] = form 
        
        return render(request, self.template_name, viewData) 
    
    def post(self, request): 
        form = ProductForm(request.POST) 
        if form.is_valid(): 
            return redirect('valido') 
        else: 
            viewData = {} 
            viewData["title"] = "Create product" 
            viewData["form"] = form 
            
            return render(request, self.template_name, viewData)
        
class ProductoValido(TemplateView):
    template_name = 'products/valido.html'