from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router=DefaultRouter()

router.register('stu',views.StudentApi,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(),name='obtain_token'),
    path('refreshtoken/', TokenRefreshView.as_view(),name='refresh_token'),
    path('verifytoken/', TokenVerifyView.as_view(),name='verify_token'),
]
