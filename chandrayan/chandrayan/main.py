from django.shortcuts import render

# Create your views here.
def mainfun(request):
    injection = {'pie':3.14,'ten':10,'letter':"o",'sentence':"neo is the one."}
    return render(request, "mainpage.html", injection)

def testing(request):
    return render(request, "rover/successpage.html")
