# fibonacciCalculator/views.py
#http://drksephy.github.io/2015/07/16/django/

from django.shortcuts import render, HttpResponse,RequestContext
import timeit
import datetime

from fibonacciCalculator.models import FibonacciNumbers

# finding fibonacci numbers using recursion
def CalcFibonacci(x):
	result = {0: 0, 1: 1}
	if x in result:
		return result[x]
	r = CalcFibonacci(x-1) + CalcFibonacci(x-2)
	result[x] = r
	return r


# Create your views here.

def index(request):
    return render(request, 'fibonacciCalculator/index.html')

def callClac(request):
    return render(request, 'fibonacciCalculator/calc.html')

def calc(request):
    calculatedData = []     
    if request.method == 'POST':
        N = int(request.POST.get('number') ) 
	t = timeit.Timer(lambda: CalcFibonacci(N))	     
        methodData = {}
	methodData['postion'] = N 
	methodData['method'] = "Recursive"	      
        methodData['number'] = CalcFibonacci(N)
        methodData['time'] = t.timeit(number=1)
	methodData['date'] = datetime.datetime.now().date() 
  	entry =  FibonacciNumbers(position = N, value = methodData['number'], time = methodData['time'], date =  methodData['date'], method = methodData['method'])
	entry.save()          
        calculatedData.append(methodData)   
    return render(request, 'fibonacciCalculator/calc.html', {'data': calculatedData})
