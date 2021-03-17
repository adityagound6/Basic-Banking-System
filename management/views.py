from django.shortcuts import render,redirect,HttpResponse
from .models import Customer,TransectionHistory

# Create your views here.
def home(request):
    return render(request,'home.html')

def viewcustomer(request):
    customer = Customer.objects.all()
    #print(customer)
    return render(request,'viewcustomer.html',{'customer':customer})

def transection(request , slug):
    #print(slug)
    slugs = slug
    to_customer = Customer.objects.all()
    from_customer = Customer.objects.get(slug = slug)
    if(request.method == "GET"):
        return render(request,'transection.html',{'to_customer':to_customer,'from_customer':from_customer,'slugs':slugs})
    
    elif(request.method == "POST"):
        from_account = from_customer.account_number
        to_account = request.POST.get('to_account')
        particulat_customer = Customer.objects.get(account_number = to_account)
        amount = request.POST.get('amount')
        amounts = float(amount)
        print(from_customer)
        if(amounts <= from_customer.current_balance):
            from_customer.current_balance = from_customer.current_balance - amounts
            from_customer.save()
            particulat_customer.current_balance = particulat_customer.current_balance + amounts
            particulat_customer.save()
            value = TransectionHistory(from_account = from_account,
                                        to_account  = to_account,
                                        amount = amounts)
            value.save()
            print(particulat_customer)
            print(particulat_customer.current_balance)
            return render(request,'home.html')
        else :
            error = "Insufficient Fund"
            return render(request ,'home.html',{'error' : error})

def transection_history(request):
    tra_hist = TransectionHistory.objects.all()
    return render(request , 'transection_history.html', {'tra_hist':tra_hist})