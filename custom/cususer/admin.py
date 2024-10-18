from django.contrib import admin
from django.contrib.auth import get_user_model

CustomeUser = get_user_model()
admin.site.register(CustomeUser)