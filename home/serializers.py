from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration 
        depth1=1
        fields=('__all__')
        # fields = ['url', 'username', 'email', 'is_staff']
        


