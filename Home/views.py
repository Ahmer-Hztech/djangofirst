from django.shortcuts import render,HttpResponse 
from datetime import datetime
from Home.models import Contact
# Create your views here.
def index(request):
    Page=request.GET.get('id')
    data={
        "page_name":"Home",
    }
    return render(request,'index.html',data)

def about(request):
    data={
        "page_name":"About"
    }
    return render(request,'about.html',data)

def contact(request):
    data={
        "page_name":"Contact"
    }
    return render(request,'contact.html',data)
    # return HttpResponse("<h2>This is Contact Us Page</h2>")

def contact_submit(request):
    name=request.POST.get('name');
    email=request.POST.get('email');
    phone=request.POST.get('phone');
    message=request.POST.get('message');
    contact =Contact(name=name,email=email,phone=phone,message=message,date=datetime.today())
    contact.save()
    # raise Exception(request.POST.get("name"))