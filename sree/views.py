from django.shortcuts import render

# Create your views here.

from datetime import date

def sr(request):
    d = {'name':'Sreenivasulu Gattu','today':date.today()}
    return render(request,'data_render.html',context=d)