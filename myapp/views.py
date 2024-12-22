from django.shortcuts import render,redirect
from django.http import HttpResponse
from service.models import Service
# from .models import UserForm


# Create your views here.

def home(request):
    servicesData=Service.objects.all()
    # for a in servicesData:
    #     print(a.service_title) 
    data={
        'servicesData':servicesData
    }

    return render(request,"index.html",data)

def about(request):
    return render(request,"aboutus.html")

def contact(request):
    return render(request,"contact.html")

def services(request):
    return render(request,"services.html")

def form(request):
    return render(request,"form.html")


def userform(request):                                    #this is for show form data in new page
    finalans=0
    fn=UserForm()
    data={'form' : fn}
    try:
        if request.method=="POST":
            n1=int(request.POST.get("num1"))
            n1=int(request.POST.get("num2"))
            finalans=n1 + n2
            data={
                'form':fn,
                'output':finalans
               
                
            }
    except:
        pass
    return render (request,"form.html",data)


def submitform(request):
    try:
        if request.method=="POST":
            n1=int(request.POST.get("num1"))
            n2=int(request.POST.get("num2"))
            finalans=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
            return HttpResponse(finalans)
    except:
        pass
    
    
    
    
def calculator(request):
    c=''
    try:
        if request.method=="POST":
            m1=eval(request.POST.get("num1"))
            m2=eval(request.POST.get("num2"))
            opr=request.POST.get("opr")
            if opr=="+":
                c=m1 + m2
            elif opr=="-":
                c=m1 - m2
                    
            elif opr=="*":
                c=m1 * m2
                    
            elif opr=="/":
                c=m1 / m2
            else:
                c = "Invalid Operator"
    except:
        c="Invalid Input"
                    
        
    return render(request,"calculator.html",{'c':c})




def evenodd(request):
    c=''
    if request.method=="POST":
        if request.POST.get("num")=="":
            return render(request,"evenodd.html",{"error":True})
        
        n=eval(request.POST.get("num"))
        if n % 2==0:
            c="Even number"
        else:
            c="Odd number"
        
    return render(request,"evenodd.html",{'c':c})



def marksheets(request):
    
    data={} 
    if request.method=="POST":
            n1=eval(request.POST.get("sub1"))
            n2=eval(request.POST.get("sub2"))
            n3=eval(request.POST.get("sub3"))
            n4=eval(request.POST.get("sub4"))
            n5=eval(request.POST.get("sub5"))
        
            total=n1+n2+n3+n4+n5
            percentage=(total/500)*100  
            
            if percentage >=60:
                division="First"
            elif 50 <= percentage < 60:
                division="second"
            elif 33 <= percentage <50:
                division="third"
            else:
                division="Fail"
            
            data={
                'total':total,
                'percentage':percentage,
                'division':division
            }
        
        
    return render(request,"marksheets.html",data)