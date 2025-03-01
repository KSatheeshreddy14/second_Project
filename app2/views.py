from django.shortcuts import render

def python(request):
    return render(request, 'python.html')

def sql(request):
    return render(request, 'sql.html')
def dummy(request):
    return render(request,'dummy.html')
