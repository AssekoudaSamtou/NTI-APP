from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render


@login_required
def view_profile(request):
    user = request.user
    # print(user)
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)
