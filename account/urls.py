from django.urls import path, include
from . import views
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from account.views import UserViewSet

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('refresh/', views.RefreshView.as_view()),
    path('', include(router.urls)),
]