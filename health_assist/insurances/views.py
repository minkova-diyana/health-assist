from django.shortcuts import render


# Create your views here.
def insurances(request):
    return render(request, 'insurances/insurances.html')
