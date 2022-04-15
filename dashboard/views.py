from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def dashboard(request):
 return render(request,'dashboard/tools/list.html')