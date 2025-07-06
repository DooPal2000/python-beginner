from rest_framework import serializers
from .models import Movie, Actor


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    opening_date = serializers.DateField()
    running_time = serializers.IntegerField()
    overview = serializers.CharField()

    # 따라서 **validated_data로 언패킹하여 각 필드에 맞게 인자를 전달해야 정상적으로 모델 인스턴스가 생성됩니다.
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    gender = serializers.CharField()
    birth_date = serializers.DateField()

    # 따라서 **validated_data로 언패킹하여 각 필드에 맞게 인자를 전달해야 정상적으로 모델 인스턴스가 생성됩니다.
    def create(self, validated_data):
        return Actor.objects.create(**validated_data)
