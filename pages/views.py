from django.shortcuts import render

# Create your views here.


def about_view(request):
    return render(request, 'about.html',{})


def index(request):
    return render(request,"index.html", {})
