from django.shortcuts import render

# Create your views here.
def belloworld(request):
    return render(request, 'belloworld.html',{})
