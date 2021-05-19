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
    path('model-test-question/', views.model_test_question, name='model-test-question'),
    path('model-test-question-view/<str:pk>/', views.update_model_test_question, name='model-test-question-view'),
    path('model-test-add/', views.add_model_test, name='model-test-add'),
    path('model-test-update/<str:pk>/', views.update_model_test,
                       name='model-test-update'),
    path('close/', ClosePageView.as_view(), name='close'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
