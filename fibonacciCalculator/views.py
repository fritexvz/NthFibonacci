# views.py

from django.shortcuts import render, HttpResponse
import timeit

# finding fibonacci numbers using dynamic programming
class dpFib(object):
    def __init__(self):
        # these are the base cases
        # in addition, this is the dict to be used for storing
        # further results
        self.__result = {0: 0, 1: 1}

    def fib(self, x):
        if x in self.__result:
            return self.__result[x]

        r = self.fib(x-1) + self.fib(x-2)
        self.__result[x] = r
        return r

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')


def profile(request):
    parsedData = []
    if request.method == 'POST':
        N = request.POST.get('number')          
        f = dpFib()
	timetaken = 5
        fibonacci = f.fib(int(N))

        userData = {}        
        userData['number'] = fibonacci
        userData['time'] = timetaken            
        parsedData.append(userData)
    return render(request, 'fibonacciCalculator/profile.html', {'data': parsedData})
