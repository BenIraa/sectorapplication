from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.welcome, name='home'),
    path('pricing/',views.pricing, name='pricing'),
    path('support/',views.support, name='homesupport'),
    path('proussd/', views.proussd, name='proussd'),
    path('registration/', views.registration, name='register'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
