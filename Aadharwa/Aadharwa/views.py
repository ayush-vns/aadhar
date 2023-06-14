from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("Hello Main")

def demo (request):
    return render(request, "create.html")