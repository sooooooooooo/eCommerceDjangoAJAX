##### backoffice app #####
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.indexBackoffice),
	url(r"^orders/$", views.readallorders),
	url(r"^products/$", views.readallproductsBackoffice),
	url(r"^orders/show/1$", views.readoneorder),
	url(r"^test$", views.simple_upload),
	url(r"^products/create$", views.createProduct),
]


