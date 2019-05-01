from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url('', include(router.urls)),
]
