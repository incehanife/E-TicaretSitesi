from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from product.models import Comment, CommentForm


def index(request):
    return HttpResponse("Product Page")

def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':  # check post
        form = CommentForm(request.POST)

        if form.is_valid():
            current_user = request.user

            data = Comment()  # create relation with model
            data.user_id = current_user.id
            data.product_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')

            messages.success(request, "Your review has ben sent. Thank you for your interest.")

            return HttpResponseRedirect(url)
    messages.warning(request, "Your comment has not been saved. Please check!")

    return HttpResponseRedirect(url)