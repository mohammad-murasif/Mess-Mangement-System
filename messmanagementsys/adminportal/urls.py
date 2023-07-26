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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include


urlpatterns = [
    path('',views.home, name='home'),
    path("login/", views.AdminLogin, name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='adminportal/login.html'), name='logout'),
    path("dashboard/",views.dashboard,name="dashboard"),
    path('addstd/',views.addstudent,name="addstudent"),
    path('View-Students/',views.view_students,name='view-students'),
    path('edit/<int:pk>',views.edit,name='editstudent'),
    path('pay/',views.PayView,name='payfee'),
    path('paydirect/<int:pk>/',views.PayDirect,name='payfee'),
    path('menu/',views.menuview,name='menu'),
    path('editmenu/<int:pk>',views.editmessmenu ,name='editmenu'),
    path('payments/',views.ViewPayments, name='payments'),
    path('invoice',views.invoice,name='invoice'),
    path('invoice/<int:std_id>/<int:trans_id>/',views.invoice,name='invoicedirect'),
    path('generateinvoice/<int:std_id>/<int:trans_id>/', views.pdf, name = 'generateinvoice'),
    





]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
