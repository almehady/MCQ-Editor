from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import ClosePageView

app_name = 'core'

urlpatterns = [
    path('', views.login_page, name='login'),
    path('login/', views.login_page, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('questions/', views.question_bank, name='questions'),
    path('question-update/<str:pk>/', views.update_question_bank, name='update-question'),
    path('model-test/', views.model_test, name='model-test'),
    path('add-to-model-test/<str:pk>/', views.update_add_model_test, name='add-model-test'),
    path('close/', ClosePageView.as_view(), name='close'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
