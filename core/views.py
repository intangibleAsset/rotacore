from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def shift(request):
    sec = request.GET.get("section","error")#returns section or 1
    




    context = {'result':sec}
    return render(request, 'core/shift.html',context)
