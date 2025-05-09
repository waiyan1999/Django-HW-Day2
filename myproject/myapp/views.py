from django.shortcuts import render
from myapp.models import Customer

# Create your views here.

def customer_data(request):
    cdata = Customer.objects.all()
    context = {'data':cdata}
    return render(request,"customer.html",context)
