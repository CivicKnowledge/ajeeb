"""ajeeb URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
import dqpoll

urlpatterns = [
    path('',RedirectView.as_view(url='dqpoll/'), name='root'),
    path('dqpoll/', include('dqpoll.urls')),
    path('admin/', admin.site.urls),
]

