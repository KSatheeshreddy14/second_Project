

from django.shortcuts import render

# Create your views here.
def devops(request):
    return render(request, 'devops.html')

def dev(request):
    return render(request, 'dev.html')

def dummy(request):
    return render(request,'dummy.html')
