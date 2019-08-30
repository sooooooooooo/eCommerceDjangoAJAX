##### login_reg_app #####
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.showlogin),
	url(r"^login$", views.login),
	url(r"^register$", views.register),
	url(r"^success$", views.success),
	url(r"^logout$", views.logout),
]