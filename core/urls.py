from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import IndexView

app_name = 'core'

urlpatterns = [
    path('', views.login_page, name='login'),
    path('index/', IndexView.as_view(), name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
