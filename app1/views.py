from django.shortcuts import render

# Create your views here.
def mdb4_parent(request):
    return render(request,'mdb4parent.html')
def child(request):
    return render(request,'child.html')