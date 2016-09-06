# views.py

from django.shortcuts import render, HttpResponse
import timeit

# finding fibonacci numbers using dynamic programming
def CalcFibonacci(x):
	result = {0: 0, 1: 1}
	if x in result:
		return result[x]
	r = CalcFibonacci(x-1) + CalcFibonacci(x-2)
	result[x] = r
	return r
#N = 6



# Create your views here.

def index(request):
    return HttpResponse('Hello World!')


def profile(request):
    parsedData = []
    if request.method == 'POST':
        N = int(request.POST.get('number') )    
        timetaken = 0
	#timetaken = timeit.timeit("fib(N)", setup="from __main__ import CalcFibonacci, N",number=1)
	t = timeit.Timer(lambda: CalcFibonacci(N))
	timetaken = t.timeit(number=1)
        fibonacci = CalcFibonacci(N)
        userData = {} 	      
        userData['number'] = fibonacci
        userData['time'] = timetaken            
        parsedData.append(userData)
    return render(request, 'fibonacciCalculator/profile.html', {'data': parsedData})
