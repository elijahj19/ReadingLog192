from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from main.models import Course, Paper, User


## PAGE GET REQUESTS

# this is the landing page logic
def splash_view(request):
    # if is logged in, this should redirect to their respective dashboard
    if request.user.is_authenticated:
        return redirect('/dashboard')
    # otherwise render the default landing page for non-logged in users
    return render(request, 'splash.html', {})

# this is the about page
def about_view(request):
    return render(request, 'about.html', {})

# this is the dashboard view for logged in users
def dashboard_view(request):
    # if user is not logged in, reroute them to signin page and display error
    if not request.user.is_authenticated:
        return redirect('/accounts?needLogin=True')
    # return the dashboard view for the user
    # TODO the logic for the page
    return render(request, 'dashboard.html', {})

# this is the HTML view for logging in signing up
def accounts_view(request):
    # if the user is already logged in, then just reroute them to their dashboard because they are already logged in
    if request.user.is_authenticated:
        return redirect('/dashboard')
    
    #
    return render(request, 'accounts.html', {})

## ----------------------------------------------------------------------------------------

## REQUESTs

# this handles a user trying to login
def login_view(request):
    # if the user is already logged in redirect them to their dashboard
    if request.user.is_authenticated:
        return redirect('/dashboard?alreadyLoggedIn=True')
    print("login", request.POST['username'], request.POST['password'])
    username, password = request.POST['username'], request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None: # if login successful
        login(request, user)
        return redirect('/dashboard')
    # else redirect because an error occurred
    return redirect('/accounts?loginError=True')

# this handles a user trying to sign up
def signup_view(request):
    # if the user is already logged in redirect them to their dashboard
    if request.user.is_authenticated:
        return redirect('/dashboard?alreadyLoggedIn=True')
    print("signup", request.POST['username'], request.POST['password'], request.POST['email'])
    # error checking if all required fields are there and user already exists with username or email
    if 'username' not in request.POST or 'password' not in request.POST or 'email' not in request.POST:
        return redirect('/accounts?missingSignupParameter=True')
    if User.objects.filter(username=request.POST['username']).exists():
        return redirect('/accounts?signupUsernameExists=True')
    if User.objects.filter(email=request.POST['email']).exists():
        return redirect('/accounts?signupEmailExists=True')
    # now try to create and login user
    try:
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email']
        )
        login(request, user)
    except:
        print('signup error')
        return redirect('/accounts?signupError=True')
    
    return redirect('/dashboard')

# handles user logging out
def logout_view(request):
    logout(request)
    print('Logout Successful')
    return redirect('/')