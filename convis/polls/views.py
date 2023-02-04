from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hellow world, this is the polls index")