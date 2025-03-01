from django.shortcuts import render

def main(request):
    return render(request,'base.html')

def course(request):
    return render(request,'course.html')