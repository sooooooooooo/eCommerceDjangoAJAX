##### backoffice app #####
from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from django.contrib import messages

# Create your views here.
def indexBackoffice(request):
	return render(request, "backoffice/dashboard.html")

def readallorders(request):
	return render(request, "backoffice/allorders.html")

def readallproductsBackoffice(request):
	return render(request, "backoffice/allproducts_dashboard.html")

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'backoffice/allproducts_dashboard.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'backoffice/allproducts_dashboard.html')

def readoneorder(request):
	return render(request, "backoffice/oneorder.html")

def createProduct(request):
	if request.method == "POST" and request.FILES["pro-image"]:
		myimg = request.FILES["pro-image"]
		fs = FileSystemStorage()
		imgname = fs.save(myimg.name, myimg)
		uploaded_img_url = fs.url(imgname)

		# need to pregenerate some categories
		# this_category = Category.objects.get()
		# newly_added_product = Product.objects.create(name = request.POST["pname"], description = request.POST["pdescription"], price = request.POST["pprice"], category)
		# return redirect("/products")
		pass