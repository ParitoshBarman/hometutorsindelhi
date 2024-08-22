from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def service(request):
    return render(request, "service.html")
def teacher(request):
    return render(request, "teacher.html")



def base(request):
    return render(request, "base.html")