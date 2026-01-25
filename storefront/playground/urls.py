# file that maps URLs to views

from django.urls import path # import path class from urls package
from . import views # to  reference the views functions
# NOTE: '.' means current folder

# Now define the urlpatterns variable (the exact same name, since django looks for it)
# this is a list of URLpattern objects
urlpatterns = [path("hello/", views.say_hello)
               ]

# a path function takes a route (the string defining the url path that you want to map to the view)
# the view function (reference it from the views file)
# other parameters
#--> returns a URLPattern Object

# this is a URLConf module 
# every 'app' has its own url conf, but that url conf should be imported back in the main 
# url conf file of the django project