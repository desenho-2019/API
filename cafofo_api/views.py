from django.shortcuts import render
from django.contrib.auth.decorators import login_required

    # Create your views here.
def loginFb(request):
    return render(request, 'login.html')

def loginGoogle(request):
    context = {
        'posts': Post.objects.order_by('-date')
        if request.user.is_authenticated else []
    }

    return render(request, 'loginGoogle.html', context)
