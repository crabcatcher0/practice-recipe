from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def home(request):
    return render(request, 'index.html')


def receipes(request):
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description
        )
        return redirect('/recepies/')

    queryset = Receipe.objects.all()
    context = {'recepies': queryset}
    return render(request, 'recepies.html', context)

def delete_receipe(request, id):
    receipe = Receipe.objects.get(id = id)
    receipe.delete()                        
    return redirect('recepies')

def list_recipe(request):
    data = Receipe.objects.all()
    return render(request, 'list.html', {'recipes': data})

def list_detail(request, id):
    detail = Receipe.objects.get(id = id)
    return render(request, 'details.html', {'recipes':detail})