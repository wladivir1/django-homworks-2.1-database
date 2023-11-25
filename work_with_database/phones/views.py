from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort_by = request.GET.get('sort')
    
    if sort_by == 'name':
        phones = phones.order_by('name')
        context = {'phones': phones}
    elif sort_by == 'min_price':
        phones = phones.order_by('price')
        context = {'phones': phones}
    elif sort_by == 'max_price':
        phones = phones.order_by('-price')
        context = {'phones': phones}
    else:
        context = {'phones': phones}
        
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
            
    return render(request, template, context)
