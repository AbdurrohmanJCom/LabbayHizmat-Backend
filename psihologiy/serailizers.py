from rest_framework import serializers

from .models import User_ish_beruvchi, User_ish_oluvchi, PassportInformation, Uzcard, Humo


class UserIshBervuchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_ish_beruvchi
        fields = '__all__'


class UserIshOluvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_ish_oluvchi
        fields = '__all__'


class PassportInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportInformation
        fields = '__all__'


class UzcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uzcard
        fields = '__all__'


class HumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humo
        fields = '__all__'
