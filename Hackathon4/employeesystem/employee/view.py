from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def details(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'unknown')
        age = request.POST.get('age', 'unknown')
        company = request.POST.get('company', 'unknown')
        gross_salary = float(request.POST.get('gross_salary', 0))
        tax = float(request.POST.get('tax', 0))
        bonus = float(request.POST.get('bonus'))
        net_salary = gross_salary - (gross_salary * tax / 100) + (gross_salary * bonus / 100)
        context = {
            'name': name,
            'net_salary': round(net_salary, 2)
        }

        return render(request, 'employee/emp_out.html', context)
    else:
        return render(request, 'employee/emp_details.html')
    
    
def jumble_words(request):
    context = {}
    if request.method == 'POST':
        word = request.POST.get('word', 'unknown')
        temp = list(word)
        random.shuffle(temp)
        word = ''.join(temp)
        context = {
            'word': word
        }
    return render(request, 'employee/jumble.html', context)
