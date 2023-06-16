from django.shortcuts import render, HttpResponse, redirect

from .models import AadharModel


def index(request):
    return HttpResponse("Hello App")

def demo(request):
    result="fill this form"
    first_name=""
    last_name=""
    age=""
    aadharno=""
    if request.GET:
            try:
                
                first_name=request.GET["first_name"]
                last_name=request.GET["last_name"]
                age=request.GET["age"]
                aadharno=request.GET["aadharno"]
                a=AadharModel()
                a.first_name=first_name
                a.last_name=last_name
                a.age=age
                a.aadharno=aadharno
                a.save()
                result="Successfully data entered"
                print(first_name,last_name,age,aadharno)
            except:
                result="Error"
                
    return render(request,"create.html",{"first_name":first_name,"last_name":last_name,"result":result})

def search (request):
    aadharno=""
    aadhars=[]
    if request.GET:
        aadharno=request.GET["aadharno"]
        aadhars = AadharModel.objects.filter(aadharno=aadharno)
        if len(aadharno) <= 0:
            aadhars = AadharModel()
        else:
            aadhars = aadhars[0]
        print(aadhars)
    return render(request, "search.html", {"aadhar": aadhars, "aadharno": aadharno})

def all (request):
     aadhars = AadharModel.objects.all()
     return render(request, "all.html", {"aadhars": aadhars})


def sessionget(request):
    key = ""
    if request.POST:
        key = request.POST["key"]
        try:
            request.session.pop(key)
        except:
            pass

    return render(request,"sessionget.html", {"key": key})

def sessionset(request):
      key = ""
      value = ""
      if request.POST:
        key = request.POST["key"]
        value = request.POST["value"]
        request.session[key] = value  
      return render(request,"sessionset.html", {"key": key, "value": value})

def sessionview(request):
    request.session["score"] = 90
    request.session["scor0e"] 
    return render(request, "sessionview.html", {"session": request.session.items()})




    
          
