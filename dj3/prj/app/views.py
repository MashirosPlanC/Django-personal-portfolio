from django.shortcuts import render
from .forms import MyForm

def temp1(request):
    word = 'thIS yEar 2023-10-1'
    date = 'September 12, 2023'
    nm = 'nm'
    list1 = [[1,2,3],[4,5,6],[7,8,9]]
    table = [
        {'name': 'John', 'age': 30},
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 35},
    ]
    product = [
        {'name': 'Apple', 'price': 10, 'color': 'blue'},
        {'name': 'google', 'price': 20, 'color': 'red'}
    ]
    return render(request, 'app/temp1.html', {'word': word, 'date':date, 'nm' :nm, 'list1':list1,'table':table, 'product':product })

def temp2(request):
    table = [
        {'name': 'John', 'age': 30},
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 35},
    ]
    return render(request, 'app/temp2.html', {'table':table})

def form(request):
    submitted_data = None
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            submitted_data = form.cleaned_data
    else:
        form = MyForm()

    return render(request, 'app/form.html',{'form': form, 'submiited_data':submitted_data})

def main(request):
    return render(request, 'app/main.html')

def skills(request):
    return render(request, 'app/skills.html')

def experience(request):
    return render(request, 'app/experience.html')

# Create your views here.
