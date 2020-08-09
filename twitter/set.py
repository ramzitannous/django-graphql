from rest_framework.serializers import Serializer

class DataClassSerializer(Serializer):
    def to_representation(self, instance):
        return super().to_representation(instance)