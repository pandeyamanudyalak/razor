from multiprocessing.pool import ApplyResult
import py_compile
from django.shortcuts import render
import razorpay

# Create your views here.

def home(request):
    if request.method=='POST':
        print(request)
        amount = int(request.POST.get('amount'))*100
        print('------------AMOUNT',amount)
        client = razorpay.Client(auth=('rzp_test_npXCCPy8sFmEOO','RJvPyFoC373j24fqenIvEQ6O'))
        payment = client.order.create({'amount':amount,"currency":"INR","payment_capture":"1"})
        order_id = payment['id']
        amount = payment['amount']  
        data = {'order_id':order_id,'amount':amount}            
        

        return render(request,'home.html',{'payment':data})
        
    
    return render(request,'index.html')


def index(request):
    return render(request,'index.html')

def success(request):
    return render(request,'success.html')

   