from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'core/index.html')

@login_required
def secret(request):
    return render(request, 'core/secret.html')
