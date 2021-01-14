from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns=[
    path('',views.welcome, name='home'),
    
    
    path('proussd/', views.proussd, name='proussd'),
    path('registration/', views.registration, name='register'),
    path('<int:id>/deleteInfos/', views.delreg, name='deleteInfos'),
    path('<int:id>/updateInfos/', views.updatereg, name='updateInfos'),
    path('reg/endpoints/', views.registerEndpoint, name='endpionts'),
    path('del/endpoints/<int:id>',views.deleteEndpoint,name='deleteEndpoint'),
    path('user-creation/', CustomAuthToken.as_view()),
    path('post-endpoint/', Posts.as_view()),
    path('send-email/', views.Sendemail, name='sendemail'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

