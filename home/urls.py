from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.welcome, name='home'),
    
    
    path('proussd/', views.proussd, name='proussd'),
    path('registration/', views.registration, name='register'),
    path('<int:id>/deleteInfos/', views.delreg, name='deleteInfos'),
    path('<int:id>/updateInfos/', views.updatereg, name='updateInfos'),
    path('reg/endpoints/', views.registerEndpoint, name='endpionts'),
    path('del/endpoints/<int:id>',views.deleteEndpoint,name='deleteEndpoint'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
