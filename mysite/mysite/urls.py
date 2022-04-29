"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from notice.views  import noticeView
from student.views import StudentViewSet



routerList = (
    (r'notice', noticeView,'notice'),
    (r'student', StudentViewSet,'student'),
)

router = routers.DefaultRouter()
for route in routerList:
    router.register(route[0],route[1],basename=route[2])

urlpatterns = [
    path('polls/',include('polls.urls')),
    path('api/',include(router.urls)),
    path('admin/', admin.site.urls),
]

