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


    # 이를 위해 파이썬 딕셔너리 타입의 함수인 get()을 사용합니다. 
    # get()은 파라미터로 키(Key)와 기본값(Default Value)을 받습니다. 
    # 만약, 딕셔너리에 키에 맞는 데이터가 존재한다면 데이터를 반환하고, 
    # 키에 맞는 데이터가 존재하지 않다면 설정한 기본값을 반환합니다.
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.opening_date = validated_data.get('opening_date', instance.opening_date)
        instance.running_time = validated_data.get('running_time', instance.running_time)
        instance.overview = validated_data.get('overview', instance.overview)
        instance.save()
        return instance


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    gender = serializers.CharField()
    birth_date = serializers.DateField()

    # 따라서 **validated_data로 언패킹하여 각 필드에 맞게 인자를 전달해야 정상적으로 모델 인스턴스가 생성됩니다.
    def create(self, validated_data):
        return Actor.objects.create(**validated_data)
