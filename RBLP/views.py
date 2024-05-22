from django.shortcuts import render

# Create your views here.

def index_gender(request):
    return render(request, 'gender/index.html')