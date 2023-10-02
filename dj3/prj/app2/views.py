from django.shortcuts import render

def temp1(request):
    return render(request, 'app2/temp1.html')

def temp2(request):
    return render(request, 'app2/temp2.html')
# Create your views here.
