from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.forms import SignUpForm
from home.models import ContactFormu, ContactFormMessage, Setting, UserProfile
from product.models import Product, Category, Images


def index(request):
    setting = Setting.objects.get(pk=4)
    sliderdata = Product.objects.all()[:5]
    category = Category.objects.all()
    images = Images.objects.get(pk=9)
    images1 = Images.objects.get(pk=10)
    images2 = Images.objects.get(pk=11)
    images3 = Images.objects.get(pk=16)
    images4 = Images.objects.get(pk=17)
    images5 = Images.objects.get(pk=18)
    images6 = Images.objects.get(pk=19)
    images7 = Images.objects.get(pk=20)
    dayproducts = Product.objects.all()[:7]
    lastproducts = Product.objects.all().order_by('-id')[:6]
    randomproducts = Product.objects.all().order_by('?')[:4]

    context={'setting': setting,
             'images': images,
             'images1': images1,
             'images3': images3,
             'images2': images2,
             'images4': images4,
             'images5': images5,
             'images6': images6,
             'images7': images7,
             'category': category,
             'page':'home',
             'sliderdata':sliderdata,
             'dayproducts':dayproducts,
             'lastproducts':lastproducts,
             'randomproducts':randomproducts}
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
    categorydata = Category.objects.get(pk=id)
    setting = Setting.objects.get(pk=4)
    products = Product.objects.filter(category_id=id)
    context = {'products': products,
               'category': category,
               'setting': setting,
               'categorydata': categorydata}
    return render(request, 'products.html', context)

def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    setting = Setting.objects.get(pk=4)
    context = {'product': product,
               'setting': setting,
               'category': category,
               'images': images}
    return render(request, 'product_detail.html',context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Error! Username or Password is wrong.")
            return HttpResponseRedirect('/login')
    setting = Setting.objects.get(pk=4)
    category = Category.objects.all()
    context = {'category': category,
               'setting': setting,}
    return render(request, 'login.html',context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/users.png"
            data.save()
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup')

    form = SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.get(pk=4)
    context = {'category': category,
               'form': form,
               'setting':setting,
               }
    return render(request, 'signup.html', context)



















