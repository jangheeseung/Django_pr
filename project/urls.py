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
from django.urls import path
import app.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.index, name='index'),
    path('app/index/', app.views.index, name='index'),
    path('app/create/', app.views.create, name='create'),
    path('app/new/', app.views.blogform, name='new'),
    path('app/<int:pk>/edit/', app.views.edit, name='edit'),
    path('app/<int:pk>/remove/', app.views.remove, name='remove'),
    path('app/<int:blog_id>', app.views.detail, name='detail'),
    path('app/hashtag/', app.views.hashtagform, name='hashtag'),
    path('app/<int:hashtag_id>/search/', app.views.search, name='search'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
