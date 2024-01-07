from django.shortcuts import render
from .models import UserR
# Create your views here.
def get_users(request):
    user=UserR.objects.all()
    context={
        "user":user
    }

    return render(request, 'configrate/users.html',context)