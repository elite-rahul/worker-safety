from rest_framework.serializers import ModelSerializer
from .models import WorkerDetails

class SerializerClass(ModelSerializer):
    class Meta:
        model = WorkerDetails
        fields = '__all__'
