from django.contrib import admin
from .models import MyUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name','password')
admin.site.register(MyUser, UserAdmin)
