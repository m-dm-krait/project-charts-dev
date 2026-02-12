from django.urls import path

import index.views as index_views


urlpatterns = [
    path('', index_views.index)
]