from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import ContactFormu, ContactFormMessage, Setting
from product.models import Product, Category


def index(request):
    setting = Setting.objects.get(pk=4)
    sliderdata = Product.objects.all()[:4]
    category=Category.objects.all()

    context={'setting': setting,
             'category': category,
             'page':'home',
             'sliderdata':sliderdata}
    return render(request, 'index.html',context)

def hakkimizda(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=4)
    context = {'setting': setting,
               'category': category}
    return render(request, 'hakkimizda.html', context)

def iletisim(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=4)
    context = {'setting': setting,
               'category': category}
    return render(request, 'iletisim.html', context)

def referanslar(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=4)
    context = {'setting': setting,
               'category': category}
    return render(request, 'referanslar.html', context)

def iletisim(request):

    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been sent successfully. Thank you!")
            return HttpResponseRedirect('/iletisim')
    category = Category.objects.all()
    setting = Setting.objects.get(pk=4)
    form = ContactFormu()
    context={'setting':setting,'form':form,'category': category}
    return render(request,'iletisim.html',context)

def category_products(request,id,slug):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=4)
    products = Product.objects.filter(category_id=id)
    context = {'products': products,'category': category,'setting': setting}
    return render(request, 'products.html', context)















