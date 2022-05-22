
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.urls import path, include
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), #Path '' => Homepage
    path('', include('eye.urls')),
    path('', include('support.urls')),
    path('account/', include('account.urls')),
    path('', include('django.contrib.auth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('main/img/favicon.png'))), #Website Favicon
]
