from django.urls import path 
from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView, ProductoValido, CartView, CartRemoveAllView

urlpatterns = [
    path("", HomePageView.as_view(), name = 'home'),
    path("about/", AboutPageView.as_view(), name = 'about'),
    path('contact', ContactPageView.as_view(), name = 'contact'),
    path('products/', ProductIndexView.as_view(), name = 'index'),
    path('products/valido', ProductoValido.as_view(), name = 'valido'),
    path('products/create', ProductCreateView.as_view(), name = 'form'),
    path('products/<str:id>', ProductShowView.as_view(), name = 'show'),
    path('cart/', CartView.as_view(), name = 'cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name = 'cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name = 'cart_removeAll'),

]