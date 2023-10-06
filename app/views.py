from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *

#fbv return string
def fbv_string(request):
    return HttpResponse('returing fbv_string')

#cbv return string
class cbv_string(View):
    def get(self,request):
        return HttpResponse('returing cbv_string')
    


#fbv return html page
def fbv_page(request):
    return render(request,'fbv_page.html')

#cbv return html page
class cbv_page(View):
    def get(self,request):
        return render(request,'cbv_page.html')
    
#inserting data using fbv
def insert_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('data is inserted')
    return render(request,'insert_fbv.html',d)

#inserting data using cbv
class insert_cbv(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'insert_cbv.html',d)
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('data is inserted')
        
        

