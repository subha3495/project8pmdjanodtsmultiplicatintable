from django.shortcuts import render
from django.shortcuts import render
def input(request):
    return render(request,'input.html')
def display(request):
    i=int(request.GET["t1"])
    j=int(request.GET["t2"])
    k=range(1,j+1)
    mydic={"tb":i,"values":k}
    return render(request,'display.html',mydic)