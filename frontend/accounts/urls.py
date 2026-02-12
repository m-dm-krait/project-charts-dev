from django.urls import path

import accounts.views as accounts_views


urlpatterns = [
    path('login/', accounts_views.login),
    path('register/', accounts_views.register)
]