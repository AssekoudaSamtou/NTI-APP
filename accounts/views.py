from django.contrib.auth.models import User
from django.shortcuts import render


def view_profile(request):
    user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)