from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    exclude = ['password', 'last_login']


admin.site.register(Profile, ProfileAdmin)
