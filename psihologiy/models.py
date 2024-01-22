import random
from datetime import datetime, timedelta
from random import random

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, User
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Foydalanuvchi uchun elektron pochta kiritilishi shart')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


# Parolni tiklash uchun usullar
class PasswordReset(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)


# Boshqa modellar yoki kerakli qo'shimchalar kiritishingiz mumkin





# telegram userlari uchun model
class User_ish_beruvchi(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    numer = models.FloatField(default=0)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


# class PasswordChangeLog(models.Model):
#     user = models.ForeignKey(User_ish_beruvchi
#     on_delete = models.CASCADE, related_name = 'password_change_logs')
#     changed_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.user.username} - {self.changed_at}"
#

class User_ish_oluvchi(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    location = models.CharField(
        max_length=255)  # yoki qo'shimcha ma'lumotlar uchun models.TextField() ishlatishingiz mumkin
    created_at = models.DateTimeField(auto_now_add=True)

#
# class PasswordChangeLog(models.Model):
#     user = models.ForeignKey(User_ish_oluvchi, on_delete=models.CASCADE, related_name='password_change_logs')
#     changed_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.user} - {self.changed_at}"


# passport malumotlarni shifrlash


class UserIshBeruvchiPassporti(models.Model):
    user = models.OneToOneField(User_ish_beruvchi, on_delete=models.CASCADE)
    tugilgan_sanasi = models.DateField()
    tugilgan_joyi = models.CharField(max_length=255)
    jinsi = models.CharField(max_length=10)
    passport_raqami = models.CharField(max_length=20)
    berilgan_sana = models.DateField()

    def __str__(self):
        return f"{self.user}'ning pasport ma'lumotlari"


class UserIshOluvchiPassporti(models.Model):
    user = models.OneToOneField(User_ish_oluvchi, on_delete=models.CASCADE)
    tugilgan_sanasi = models.DateField()
    tugilgan_joyi = models.CharField(max_length=255)
    jinsi = models.CharField(max_length=10)
    passport_raqami = models.CharField(max_length=20)
    berilgan_sana = models.DateField()

    def __str__(self):
        return f"{self.user}'ning pasport ma'lumotlari"


# online tolov qilish kartalari modeli 👇


def generate_card_number_humo():
    prefix = 9600
    bank_number = random.randint(1000, 9999)
    user_number = random.randint(10000000, 99999999)
    return prefix * (10 ** 12) + bank_number * (10 ** 8) + user_number


def generate_card_number_uzcard():
    prefix = 8600
    bank_number = random.randint(1000, 9999)
    user_number = random.randint(10000000, 99999999)
    return prefix * (10 ** 12) + bank_number * (10 ** 8) + user_number


class Uzcard(models.Model):
    card_holder = models.CharField(max_length=35)
    number = models.IntegerField(default=generate_card_number_uzcard)
    expire = models.DateField(default=datetime.now() + timedelta(days=4 * 365))
    sms_notification_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.number)


class Humo(models.Model):
    card_holder = models.CharField(max_length=30)
    number = models.IntegerField(default=generate_card_number_humo)
    expire = models.DateField(default=datetime.now() + timedelta(days=4 * 365))
    sms_notification_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.number)


"""web sayt uchun model pastki qismda"""

#
#
# class Xizmat(models.Model):
#     nomi = models.CharField(max_length=255)
#     malumotlar = models.TextField()
#
# class Haqimizda(models.Model):
#     faoliyat_malumotlari = models.TextField()
#     yonalishlar = models.TextField()
#     imtiyozlar = models.TextField()
#     xizmat_imtiyozlari = models.TextField()
#     obuna_takliflari_havolasi = models.URLField()
#     ijtimoiy_tarmoqlar_havolasi = models.URLField()
#
# class Galereya(models.Model):
#     ism = models.CharField(max_length=255)
#     tasvir = models.ImageField(upload_to='galereya/')
#
# class Natijalar(models.Model):
#     ish_natijalari = models.TextField()
#     fotosurat = models.ImageField(upload_to='natijalar/')
#     mijoz_sharhi = models.TextField()
#
# class Kontaktlar(models.Model):
#     telefon_raqam = models.CharField(max_length=15)
#     manzil = models.CharField(max_length=255)
#     elektron_pochta = models.EmailField()
#     joylashuv_xaritasi = models.URLField()
#
# class Ijrochi(models.Model):
#     telefon_raqam = models.CharField(max_length=15)
#     manzil = models.CharField(max_length=255)
#     elektron_pochta = models.EmailField()
#     joylashuv_xaritasi = models.URLField()
#
# # Boshqa model uchun ham shunday yaratishingiz mumkin
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User_ish_oluvchi,User_ish_beruvchi, on_delete=models.CASCADE)
#     # Boshqa ma'lumotlar
#
# # Ro'yxatdan o'tish uchun standart User modelni ishlatishingiz mumkin
#
#
#
