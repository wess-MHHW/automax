from email import message
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View

# Create your views here.
def log_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request,data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request=request,user=user)
                messages.success(request,f"You are logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request,f"An error has occurred during login.")
        else:
            messages.error(request,f"An error has occurred during login.")

    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request,'views/login.html',{'login_form':login_form})

class RegisterView(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request,'views/register.html',{'register_form':register_form})

    def post(self,request):
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request=request,user=user)
            messages.success(request,f"User {user.username} registered successfully.")
            return redirect('home')
        else:
            messages.error(request,f"An error has occurred during registration.")
            return render(request,'views/register.html',{'register_form':register_form})