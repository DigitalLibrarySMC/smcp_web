from rest_framework.serializers import ModelSerializer
from base.models import person

class personSerializer(ModelSerializer):
    class Meta:
        model = person
        fields = '__all__'