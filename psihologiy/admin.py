# labbayhismatizda/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, PasswordChangeLog
from .models import User_ish_beruvchi, User_ish_oluvchi, PassportInformation, Uzcard, Humo

admin.site.register(User_ish_beruvchi)
admin.site.register(User_ish_oluvchi)
admin.site.register(PassportInformation)
admin.site.register(Uzcard)
admin.site.register(Humo)


# class PasswordChangeLogInline(admin.TabularInline):
#     model = PasswordChangeLog
#     extra = 0
#
#
# class CustomUserAdmin(UserAdmin):
#     inlines = [PasswordChangeLogInline]
#
#
# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(PasswordChangeLog)
