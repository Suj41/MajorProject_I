from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'LandingPage.html')
def signup(request):
    return render(request,'UserRegistration.html')
def login(request):
    return render(request,'Login.html')

def user(request):
    return render(request, 'UserRegistration.html')
def department(request):
    return render(request,'DepartmentRegistration.html')
def dashboard(request):
    return render(request,'Dashboard.html')
def product(request):
    return render(request,'Product.html')
def vendor(request):
    return render(request,'Vendor.html')
def warehouse(request):
    return render(request,'Warehouse.html')
def transaction(request):
    return render(request,'Transaction.html')
def order(request):
    return render(request,'Order.html')
def customer(request):
    return render(request,'Customer.html')