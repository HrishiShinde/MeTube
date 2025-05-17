from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.contrib import messages

User = get_user_model()

# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match, baby 😤")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken 😩")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken, try again sweetheart 😩")
            return redirect('register')

        user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
        user.save()
        login(request, user)
        messages.success(request, f"Welcome to MeTube, {username}! 💃🏽✨")
        return redirect('/')
    return render(request, 'registration/register.html')