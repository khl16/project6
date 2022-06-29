from django.shortcuts import render,HttpResponse,redirect 

import random
# Create your views here.



def index(request):
    if "number" in request.session:
        number = request.session["number"]
    else:
        number = 0
        request.session["number"] = 0
    
    request.session["number"] = random.randint(1, 100)
    return render (request , 'index.html')

def result(request):
    print("random num: ", request.session['number'])
    guess=request.POST['guess']
    number=request.session['number']
    context={
        "guess" : guess,
        "number" : number
    }
    return render (request ,'show.html',context)

def newgame(request):
    del request.session['counter']
    return redirect('/')
    