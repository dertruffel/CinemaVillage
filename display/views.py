from django.shortcuts import render

# Create your views here.


def index(request):
    #return HttpResponse("Index")
    return render(request,template_name='display/base.html')