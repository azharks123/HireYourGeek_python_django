"""hireyourgeekpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from hireyourgeekapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('buyerhome', views.buyerhome, name='buyerhome'),
    path('coderhome', views.coderhome, name='coderhome'),
    path('buyerreg', views.buyerreg, name='buyerreg'),
    path('coderreg', views.coderreg, name='coderreg'),
    path('login/', views.login, name='login'),
    path('adminviewbuyer', views.adminviewbuyer, name='adminviewbuyer'),
    path('adminviewcoder', views.adminviewcoder, name='adminviewcoder'),
    path('adminupdatebuyer', views.adminupdatebuyer, name='adminupdatebuyer'),
    path('adminupdatecoder', views.adminupdatecoder, name='adminupdatecoder'),
    path('buyerviewprofile', views.buyerviewprofile, name='buyerviewprofile'),
    path('buyeraddrequest', views.buyeraddrequest, name='buyeraddrequest'),
    path('coderviewrequest', views.coderviewrequest, name='coderviewrequest'),
    path('coderaddbid', views.coderaddbid, name='coderaddbid'),
    path('coderviewbid', views.coderviewbid, name='coderviewbid'),
    path('coderviewwork', views.coderviewwork, name='coderviewwork'),
    path('coderupdateproject', views.coderupdateproject, name='coderupdateproject'),
    path('buyerviewworkproject', views.buyerviewworkproject,
         name='buyerviewworkproject'),
    path('buyerviewbid', views.buyerviewbid, name='buyerviewbid'),
    path('buyerviewbidfirst', views.buyerviewbidfirst, name='buyerviewbidfirst'),
    path('buyerconformbid', views.buyerconformbid, name='buyerconformbid'),
    path('buyerviewworkstatus', views.buyerviewworkstatus,
         name='buyerviewworkstatus'),
    path('buyermakepayment', views.buyermakepayment, name='buyermakepayment'),
    path('coderupdateworkstatus', views.coderupdateworkstatus,
         name='coderupdateworkstatus'),
    path('buyerviewpayment', views.buyerviewpayment, name='buyerviewpayment'),
    path('coderviewpayment', views.coderviewpayment, name='coderviewpayment'),
    path('coderviewprofile', views.coderviewprofile, name='coderviewprofile'),
]
