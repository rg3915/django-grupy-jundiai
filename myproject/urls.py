"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from myproject.bands import views as v
from django.contrib import admin

app_name = 'bands'

urlpatterns = [
    path('', v.home, name='home'),
    path('bands/', v.band_list, name='bands'),
    path('bands/<int:pk>/', v.band_detail, name='band_detail'),
    path('bandform/', v.BandCreate.as_view(), name='band_form'),
    path('bands/create/', v.band_create, name='band_create'),

    # path('members/', v.members, name='members'),
    path('members/', v.MemberList.as_view(), name='members'),
    path('members/add/ajax/', v.members_add_ajax, name='members_add_ajax'),
    path('members/json/', v.members_json, name='members_json'),
    path('memberform/', v.MemberCreate.as_view(), name='member_form'),
    path('members_vue/', v.members_vue, name='members_vue'),

    path('my_send_email/', v.my_send_email, name='my_send_email'),
    path('contact/', v.band_contact, name='contact'),
    path('contact/as_p/', v.band_contact_as_p, name='contact_as_p'),
    path('contact/as_table/', v.band_contact_as_table, name='contact_as_table'),
    path('contact/bootstrap/', v.band_contact_bootstrap, name='contact_bootstrap'),
    path('contact/crispy/', v.band_contact_crispy, name='contact_crispy'),

    path('protected/', v.protected_view, name='protected'),
    path('accounts/login/', v.message),
    path('admin/', admin.site.urls),
]
