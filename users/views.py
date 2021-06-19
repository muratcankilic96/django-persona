from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            arcana = form.cleaned_data.get('arcana')
            user.profile.arcana = arcana
            user.save()
            messages.success(request, f'Your path has been drawn, {username} of {arcana}.')
            return redirect('login')
        else:
            messages.info(request, f'Death is not an end...')           
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', 
    {'form' : form, 
    'title': 'Entering into the Realm Between Mind and Matter'}
    )

@login_required
def profile(request):
    if request.method == 'POST':    
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
        request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            arcana = p_form.cleaned_data.get('arcana')
            messages.success(request, f'Your path has been altered, {username} of {arcana}.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': "ようこそ、わがベルベットルームへ"
    }

    return render(request, 'users/profile.html', context)