from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customers
from .models import Transactions
# Create your views here.


def home(request):
    
    return render(request, 'home.html')


def all_customers(request):
    customer=Customers.objects.all()
    content={'customer':customer}
    return render(request, 'all_customers.html',content)


def transfer(request):
    if request.method=='POST':
        customer=Customers.objects.all()
        transactions=Transactions()
        for i in customer:
            sender=request.POST.get('sender')
            receiver=request.POST.get('receiver')
            amount=request.POST.get('amount')
            if i.account_no == sender:
                i.balance = i.balance-int(amount)
            if i.account_no == receiver:
                i.balance = i.balance+int(amount)
            i.save()
        sender=request.POST.get('sender')
        receiver=request.POST.get('receiver')
        amount=request.POST.get('amount')
        transactions.sender = sender
        transactions.receiver = receiver
        transactions.amount=amount
        transactions.save()
        return redirect('all_customers')
    return render(request, 'transfer.html')
