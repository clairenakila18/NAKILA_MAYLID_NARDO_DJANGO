from django.shortcuts import render

def index (request):
    context={}
    return render (request, "myApp/index.html", context)
