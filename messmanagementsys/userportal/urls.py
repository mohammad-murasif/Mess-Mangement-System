"""messmanagementsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('udashboard/',views.dashboard, name='u-dashboard'),
    path('payments/',views.payments, name='u-payments'),
    path('umenu/',views.messmenu,name='u-menu'),
    path('ulogin/',views.userlogin, name='u-login'),
    path('',views.home, name='home'),
    path('uprofile',views.profile , name="u-profile"),
    path("ulogout/", auth_views.LogoutView.as_view(template_name='userportal/home.html'), name='u-logout'),
    path('changepass', views.change_password, name='change_password'),
    path('applyleave/',views.applyleave,name='u-leave')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
