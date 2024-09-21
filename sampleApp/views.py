from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from sampleApp.form import *


# Create your views here.

class homepage(View):
    def get(self, request):
        return render(request, "shop/index.html")
    
class loginpage(View):
    def get(self, request):
        return render(request, "admin 2/form.html")
class adminDashboard(View):
    def get(self, request):
        return render(request, "shop/adminDashboard.html" )
class reply(View):
    def get(self,request):
        return render(request, "admin 2/reply.html")
    

    
class shop(View):
    def get(self,request):
        return render(request, "admin 2/shop.html")
  
        
class Addproduct(View):
    def get(self,request):
        return render(request,'shop/addProduct.html')
    def post(self, request):
        form = RegisterProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("registered");window.location("/")</script>''')

class Addoffer(View):
    def get(self,request):
        return render(request, 'shop/addoffer.html')
    def post(self,request):
        form =AddofferForm (request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("registered");window.location("/")</script>''')
        
        
            