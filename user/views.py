
from django.shortcuts import render

# Create your views here.
from home.models import Setting, UserProfile
from product.models import Category


def index(request):
    setting = Setting.objects.get(pk=4)
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)

    context = {'profile': profile,
               'setting': setting,
               'category': category,}
    return render(request,'user_profile.html',context)