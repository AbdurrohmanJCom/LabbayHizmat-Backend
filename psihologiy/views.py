from rest_framework import generics

from .models import User_ish_beruvchi, User_ish_oluvchi, PassportInformation, Uzcard, Humo
from .serailizers import UserIshBervuchiSerializer, UserIshOluvchiSerializer, PassportInformationSerializer, \
    UzcardSerializer, HumoSerializer


class UserIshBervuchiList(generics.ListCreateAPIView):
    queryset = User_ish_beruvchi.objects.all()
    serializer_class = UserIshBervuchiSerializer


class UserIshBervuchiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_ish_beruvchi.objects.all()
    serializer_class = UserIshBervuchiSerializer


class UserIshOluvchiList(generics.ListCreateAPIView):
    queryset = User_ish_oluvchi.objects.all()
    serializer_class = UserIshOluvchiSerializer


class UserIshOluvchiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_ish_oluvchi.objects.all()
    serializer_class = UserIshOluvchiSerializer


class PassportInformationList(generics.ListCreateAPIView):
    queryset = PassportInformation.objects.all()
    serializer_class = PassportInformationSerializer


class PassportInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PassportInformation.objects.all()
    serializer_class = PassportInformationSerializer


class UzcardList(generics.ListCreateAPIView):
    queryset = Uzcard.objects.all()
    serializer_class = UzcardSerializer


class UzcardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Uzcard.objects.all()
    serializer_class = UzcardSerializer


class HumoList(generics.ListCreateAPIView):
    queryset = Humo.objects.all()
    serializer_class = HumoSerializer


class HumoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Humo.objects.all()
    serializer_class = HumoSerializer
