##### storefront app #####
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.indexStorefront),
	url(r"^products/$", views.allprodStorefront),
	url(r"^products/show/1$", views.readoneStorefront),
	url(r"^carts/$", views.checkout),
	url(r"^login$", views.customerLogin),
	url(r"^register$", views.customerRegister),
	url(r"^logout$", views.customerLogout),
]