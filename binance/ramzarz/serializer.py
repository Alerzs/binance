from rest_framework.serializers import ModelSerializer
from .models import Shart

class ShartSerializer(ModelSerializer):
    class Meta:
        model = Shart
        exclude = ['user']
    