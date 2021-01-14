from rest_framework import serializers
from .models import *


from django.core.mail import send_mail
from django.conf import settings

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration 
        depth1=1
        fields=('__all__')
        # fields = ['url', 'username', 'email', 'is_staff']

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Posts
        depth=1
        fields = ('__all__')
        

class SendemailSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sendemail
        depth =1
        fields = ('__all__')
    def create(self,validated_data):
        subject=str(validated_data['subject'])
        message=str(validated_data['description'])
        from_email=settings.EMAIL_HOST_USER
        send_mail(subject,message,from_email,[str(validated_data['email'])],fail_silently=False)
    
    
     