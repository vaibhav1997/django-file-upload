from django.http import HttpResponse
from django.shortcuts import render
from .models import Name ,File 
# Create your views here.
# def index(request):
#     return HttpResponse("Hello World!")
def greet(request):
    total_name = Name.objects.all().get(id=2)
    # last_name = Name.objects.all().get(id=1)
    # context = {
    #     'first_name': first_name,
    #     'last_name': last_name,
    #     }
    return render(request, 'index.html', {'name': total_name})

def accept(request):
    fn = request.POST['fn']
    ln = request.POST['ln']
    Name.objects.create(firstName = fn, lastName = ln)
    return render(request, 'index.html')
