from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import WallPaper
from .forms import WallForm
from django.urls import reverse

def index(request):
    display = WallPaper.objects.all()
    return render(request, 'index.html', {'display': display})


def home_view(request):
    if request.method == "POST":
        wform = WallForm(request.POST, request.FILES)
        if wform.is_valid():
            wform.save()
            return redirect('/index')
    else:
        wform = WallForm()
    return render(request, "home.html", {'wform': wform})

def detail(request, id):
    order = get_object_or_404(WallPaper, pk=id)
    return render(request, 'detail.html', {'order': order})

def delete(request, id):
    un_order = get_object_or_404(WallPaper, pk=id)
    un_order.delete()
    return HttpResponseRedirect(reverse('index', args =(un_order.id,)))