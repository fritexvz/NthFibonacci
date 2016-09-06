# NthFibonacci/urls.py
# Within root URLs file within the NthFibonacci folder, we'll configure our urls to be proceeded by fibonacciCalculator/:

from django.conf.urls import include, url
from django.contrib import admin

# Now, urls can be accesses at http://127.0.0.1:8000/fibonacciCalculator/<view url>
urlpatterns = [
  url(r'^fibonacciCalculator/', include('fibonacciCalculator.urls')),
  url(r'^admin/', include(admin.site.urls)),
]
