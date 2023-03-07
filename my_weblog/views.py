from django.shortcuts import render

def home(req):
    return render(req,'my_weblog/index.html')

# Create your views here.
