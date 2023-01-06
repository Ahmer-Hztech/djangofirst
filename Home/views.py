from django.shortcuts import render,HttpResponse 

# Create your views here.
def index(request):
    Page=request.GET.get('id')
    return render(request,'index.html')

def about(request):
    data={
        "test_1":"TEST",
        "test_2":"TEST 2",
        "test_3":"TEST 3",
    }
    return render(request,'about.html',data)

def contact(request):
    return HttpResponse("<h2>This is Contact Us Page</h2>")