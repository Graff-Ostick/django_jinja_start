from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'hjinja/home.html')

def contact(request):
    return render(request, 'hjinja/basic.html', {'values' :['if you have any question please call in this phone ', '06521155']})

