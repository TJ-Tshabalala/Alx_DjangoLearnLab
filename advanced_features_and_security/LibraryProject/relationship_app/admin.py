from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomerUserAdmin(UserAdmin):
    pass

admin.site.register(CustomUser, CustomerUserAdmin)
# Register your models here.
