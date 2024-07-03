from django.shortcuts import render
from .models import Account, Comment

def index(request):
    accounts = Account.objects.all()
    comments = Comment.objects.all()
    context = {
        'accounts': accounts,
        'comments': comments,
    }
    return render(request, 'index.html', context)
