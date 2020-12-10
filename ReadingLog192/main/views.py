from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


## PAGE GET REQUESTS

# this is the landing page logic
def splash_view(request):
    # if is logged in, this should redirect to their respective dashboard
    if request.user.is_authenticated:
        return redirect('/dashboard')
    # otherwise render the default landing page for non-logged in users
    return render(request, 'splash.html', {})

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
    # TODO
    return redirect('/dashboard')

# this handles a user trying to sign up
def signup_view(request):
    # TODO
    return redirect('/dashboard')