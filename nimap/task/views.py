from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from.models import User, Client, Project ,Userproject
from django.conf import settings
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


from rest_framework import viewsets
from rest_framework import permissions
from task.serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer



def userreg(request):
    if request.method=="POST":
        r=User(username=request.POST["username"],emailid=request.POST["emailid"],password=request.POST["password"],mobileno=request.POST["mobileno"],location=request.POST["location"])
        r.save()
        return render(request,"task/userreg.html",{"res":"data insertion successfully"})
    return render(request,"task/userreg.html")

def login(request):
    if request.method=="POST":
        a = User.objects.filter(emailid=request.POST["emailid"], password=request.POST["password"])
        if a.count()>0:
            request.session["sessuid"]=request.POST["emailid"]
            if request.POST.get("chk"):
                response = HttpResponse(status=302)
                response.set_cookie('ckey',request.POST["emailid"])
                response.set_cookie('ckey1',request.POST["password"])
                response['Location']='project'
                return response
            
        else:
            return render(request,"task/login.html",{"res":"invalid userid and password"})
    else:
        cookie1=""
        cookie2=""
    if request.COOKIES.get("ckey"):
        cookie1=request.COOKIES["ckey"]
        cookie2=request.COOKIES["ckey1"]

    return render(request,"task/login.html",{"ucookie":cookie1,"pcookie":cookie2})

def logout(request):
    response=HttpResponse(status=302)
    response.delete_cookie("ckey","/")
    response.delete_cookie("ckey1","/")
    del  request.session["sessuid"]
    response['Location']='home'
    return response


class ClientCreate(CreateView):
    model = Client
    fields = ['name','companyname','title','emailid','password','phonenumber','address','city','state','postalcode']
    success_url="/task/clientlist"

class ClientList(ListView):
    model = Client
    success_url="/task/clientlist"

class ClientUpdate(UpdateView):
    model = Client
    fields = ['name','companyname','title','emailid','password','phonenumber','address','city','state','postalcode']
    success_url="/task/clientlist"

class ClientDelete(DeleteView):
    model = Client
    success_url = '/task/clientlist'

def project(request):
    if(request.session.has_key('sessuid')):
        suid=request.session['sessuid']
        data = Project.objects.all()
        return render(request,"task/project.html",{"res1":data})
    else:
        return redirect('login') 


def assign(request):
    d1=Client.objects.all()
    d2=Project.objects.all()
    
    return render(request,"task/assign.html",{"res1":d1,"res2":d2})

def projectinsert(request):
    if request.method=="POST":
        r = Project(projectname=request.POST["projectname1"],
            projectdiscription=request.POST["projectdiscription"],projecttechnology=request.POST["projecttechnology"])
        r.save()
        return render(request,"task/projectinsert.html",{"res1":Project.objects.all()})
    return render(request,"task/projectinsert.html",{"res1":Project.objects.all()})




def home(request):
    
    return render(request,"task/home.html")

def clientreg(request):
     if request.method=="POST":
        r=Client(name=request.POST["name"],companyname=request.POST["companyname"],title=request.POST["title"],emailid=request.POST["emailid"],password=request.POST["password"],phonenumber=request.POST["phonenumber"],address=request.POST["address"],city=request.POST["city"],state=request.POST["state"],postalcode=request.POST["postalcode"])
        r.save()
        return render(request,"task/clientreg.html",{"res":"data insertion successfully"})
     return render(request,"task/clientreg.html")

def clientlogin(request):
    if request.method=="POST":
        a = Client.objects.filter(emailid=request.POST["emailid"], password=request.POST["password"])
        if a.count()>0:
            request.session["sessuid"]=request.POST["emailid"]
            if request.POST.get("chk"):
                response = HttpResponse(status=302)
                response.set_cookie('ckey',request.POST["emailid"])
                response.set_cookie('ckey1',request.POST["password"])
                response['Location']='assign'
                return response
            
        else:
            return render(request,"task/clientlogin.html",{"res":"invalid userid and password"})
    else:
        cookie1=""
        cookie2=""
    if request.COOKIES.get("ckey"):
        cookie1=request.COOKIES["ckey"]
        cookie2=request.COOKIES["ckey1"]

    return render(request,"task/clientlogin.html",{"ucookie":cookie1,"pcookie":cookie2})





   
    


   

