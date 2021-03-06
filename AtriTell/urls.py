from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.index),
    path('post', views.post_create),
    path('auth', views.account_auth),
    path('register', views.account_register),
    path('logout/', views.account_logout),
    path('account', views.account_settings),
    path('<str:user_name>/<str:post_url>/', views.post_get_or_save),
    path('integrations/<str:service>', views.integrations),
    path('webhooks/<str:service>', csrf_exempt(views.web_hooks))
]
