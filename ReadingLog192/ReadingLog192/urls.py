"""ReadingLog192 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import splash_view, about_view, dashboard_view, accounts_view, login_view, signup_view, logout_view, progress_view, classes_view, authors_view, authorReadings_view, classReadings_view, readingProgress_view, readingStats_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', splash_view),
    path('about/', about_view),
    path('dashboard/', dashboard_view),
    path('accounts/', accounts_view),
    path('classes/', classes_view),
    path('authors/', authors_view),
    path('authorReadings/', authorReadings_view),
    path('classReadings/', classReadings_view),
    path('readingProgress/', readingProgress_view),
    path('readingStats/', readingStats_view),

    path('login/', login_view, name='login_view'),
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view, name='logout_view'),
    path('progress/', progress_view, name='progress_view')
]
