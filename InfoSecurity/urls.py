"""InfoSecurity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from Accounts.views import admin_login

from django.conf import settings
from django.conf.urls.static import static

admin.site.index_template = 'admin/custom_index.html'

urlpatterns = [
    path('admin/login/', admin_login),
    path('admin/', admin.site.urls),
    path('accounts/', include(('Accounts.urls', 'Accounts'), namespace='accounts')),
    path('security/', include(('Skzi.urls', 'Skzi'), namespace='skzi')),
    path('ispdn/', include(('Ispdn.urls', 'Ispdn'), namespace='ispdn')),
    path('other/', include(('Pdn.urls', 'Pdn'), namespace='pdn')),
    path('other/', include(('Other.urls', 'Other'), namespace='other')),
    path('', include(('Main.urls', 'Main'), namespace='main')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
