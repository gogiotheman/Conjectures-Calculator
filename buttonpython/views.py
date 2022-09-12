from django.shortcuts import render
import requests


def button(request):
    return render(request, 'atestat.html')

def collatz(request):
    n=request.POST.get('param')
    a=int(n,base=10)
    lista=[a,]
    while a>1:
        if a%2==0:
            a=a//2
        else:
            a=3*a+1
        lista.append(a)
    return render(request,'atestat.html',{'data':lista})

def persmult(request):
	k=0
	a=request.POST.get('m')
	n=int(a,base=10)
	lista1=[n,]
	while n>=10:
		p=1
		while n>0:
			p=p*(n%10)
			n=n//10
		n=p
		lista1.append(n)
		k=k+1
	return render(request,'atestat.html',{'data1':lista1, 'data2':k})

def goldbach(request):
	nrCitit = request.POST.get('paramGoldbach')
	nr = int(nrCitit, base = 10)

	
	

