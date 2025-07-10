from rest_framework import serializers
from .models import Movie, Actor
from django.core.validators import MaxLengthValidator, MinLengthValidator
from rest_framework.serializers import ValidationError
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator


def overview_validator(value):  # 별도로 함수를 만들어 사용
    if value > 300:
        raise ValidationError("소개 문구는 최대 300자 이하로 작성해야 합니다.")
    elif value < 10:
        raise ValidationError("소개 문구는 최소 10자 이상으로 작성해야 합니다.")
    return value


class MovieSerializer_bk(serializers.Serializer):
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
        instance.name = validated_data.get("name", instance.name)
        instance.opening_date = validated_data.get(
            "opening_date", instance.opening_date
        )
        instance.running_time = validated_data.get(
            "running_time", instance.running_time
        )
        instance.overview = validated_data.get("overview", instance.overview)
        instance.save()
        return instance


class MovieSerializer(serializers.ModelSerializer):
    # 위 내용과 동일하지만, ModelSerializer 사용하여 create 및 update 내장
    name = serializers.CharField(validators=[UniqueValidator(
    queryset=Movie.objects.all(),
    message='이미 존재하는 영화 이름입니다.',
    )])

    class Meta:
        model = Movie
        fields = ["id", "name", "opening_date", "running_time", "overview"]

        # 1. overview = serializers.CharField(
        #     validators=[
        #         MinLengthValidator(limit_value=10),
        #         MaxLengthValidator(limit_value=300),
        #     ]
        # ) 이 방식 혹은 아래 방식
        
        # 2. overview = serializers.CharField(validators=[overview_validator])
        
        validators = [
            UniqueTogetherValidator( # 3. 두 개 이상의 필드에서 값이 유일한지 확인해 주는 validator, 이름이 같아도 소개문구 다르면 생성 가능
                queryset=Movie.objects.all(),
                fields=['name', 'overview'],
            )
        ]



class ActorSerializer_bk(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    gender = serializers.CharField()
    birth_date = serializers.DateField()

    # 따라서 **validated_data로 언패킹하여 각 필드에 맞게 인자를 전달해야 정상적으로 모델 인스턴스가 생성됩니다.
    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.save()
        return instance


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["name", "gender", "birth_date"]
        # extra_kwargs = { extra_kwargs 학습 예제
        #     'birth_date': {'write_only': True},
        # }
