from django.shortcuts import render

# Create your views here.
from datetime import date
def si(request):
    d = {'name':'Siva Sankar Babu','today':date.today()}
    
    return render(request,'data_render.html',context=d)