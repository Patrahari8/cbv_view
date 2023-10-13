from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy
# Create your views here.

class Schoollist(ListView):
    model=School
    context_object_name='sclist'

class Schooldetail(DetailView):
    model=School
    context_object_name='schoolobj'

class Schoolcreate(CreateView):
    model=School
    fields='__all__'

class Schoolupdate(UpdateView):
    model=School
    fields='__all__'

class Schooldelete(DeleteView):
    model=School
    context_object_name='schoolobject'
    success_url=reverse_lazy('Schoollist')
    