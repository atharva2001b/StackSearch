from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, 'Index.html')

def search(req):

    val = req.GET.get('sQuerry')

    return render(req, 'search.html', {'value': val})