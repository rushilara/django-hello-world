from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello, world!")


def  badly_formatted( x ):
    return x
