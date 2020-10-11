"""unit URL Configuration

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
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from API.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   path('', include(router.urls)),
   path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
   path('admin/', admin.site.urls),
   path('add_item/', add_item),
   path('register_new_charity/', register_new_charity),
   path('login_new_charity/',login_new_charity),
   path('login_user/',login_user),
   path('get_all_charities/', get_all_charities),
   path('get_all_items_by_charity/',get_all_items_by_charity),
   path('order_new_item/',order_new_item),
   path('modify_charity_details/',modify_charity_details),
   path('get_charity_participants/',get_charity_participants),
   path('delete_item/',delete_item),
]
