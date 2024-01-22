from django.urls import path
from .views import UserIshBervuchiList, UserIshBervuchiDetail, UserIshOluvchiList, UserIshOluvchiDetail, PassportInformationList, PassportInformationDetail, UzcardList, UzcardDetail, HumoList, HumoDetail

urlpatterns = [
    path('user_ish_beruvchi/', UserIshBervuchiList.as_view(), name='user_ish_beruvchi_list'),
    path('user_ish_beruvchi/<int:pk>/', UserIshBervuchiDetail.as_view(), name='user_ish_beruvchi_detail'),

    path('user_ish_oluvchi/', UserIshOluvchiList.as_view(), name='user_ish_oluvchi_list'),
    path('user_ish_oluvchi/<int:pk>/', UserIshOluvchiDetail.as_view(), name='user_ish_oluvchi_detail'),

    # path('passport_information/', PassportInformationList.as_view(), name='passport_information_list'),
    # path('passport_information/<int:pk>/', PassportInformationDetail.as_view(), name='passport_information_detail'),
    #
    # path('uzcard/', UzcardList.as_view(), name='uzcard_list'),
    # path('uzcard/<int:pk>/', UzcardDetail.as_view(), name='uzcard_detail'),
    #
    # path('humo/', HumoList.as_view(), name='humo_list'),
    # path('humo/<int:pk>/', HumoDetail.as_view(), name='humo_detail'),
]
