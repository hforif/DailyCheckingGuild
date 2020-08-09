from django.shortcuts import render, redirect
from accounts.forms import SignupForm
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


def accounts_main(request):
    return render(request, 'accounts/main.html')