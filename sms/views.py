from django.shortcuts import render

# Create your views here.
def base(request):
   return render(request,'sms/base.html')


def ThreadView(request):
   return render(request,'sms/ThreadView.html')


def home(request):
   return render(request,'sms/inbox.html')


