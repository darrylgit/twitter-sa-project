"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url

"""
Remove local media helper function in production
"""
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'', include('apps.analysis.urls', namespace='analysis'), name='index'),
    url(r'^auth/', include('apps.authentication.urls', namespace='auth')),
    url(r'^dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
    url('admin/', admin.site.urls),
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
