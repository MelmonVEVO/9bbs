"""
URL configuration for bbs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework import routers
from boards.views import BoardApi, PostsInThread, UserApi

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'boards/?', BoardApi)
router.register(r'users/?', UserApi)

urlpatterns = [
    path('', include('frontend_serve.urls')),
    path('api/', include(router.urls)),
    path('api/thread/<int:pk>', PostsInThread.as_view(), name='posts-in-thread'),
    # path('api/board/<str:board>', ThreadsInBoard.as_view(), name='threads-in-board'),
    path('admin/', admin.site.urls),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
