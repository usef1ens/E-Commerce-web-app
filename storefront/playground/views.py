from django.shortcuts import render
from django.http import HttpResponse # import the HttpResponse class from django's http package
# Create your views here.
# view functions: takes a request --> returns a response
# these functions are request handlers
# in some frameworks, it is called an 'action'


# a function that takes a request object and returns hello
def say_hello(request): 
   # return HttpResponse("Hello World") # return a response with the string 'Hello World'
   return render(request, 'hello.html', {'name': 'Youssef'})
# instead of returning a plain HttpResponse object, render the corresponding html
# how will this function be called? once you map this view to a URL, then when we have a request 
# to that URL, the function will be called
#method;
# make a urls file in the 'app's directory 




