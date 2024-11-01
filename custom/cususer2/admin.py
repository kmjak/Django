from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _

from cususer2.models import Employee
# Register your models here.

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Employee
        fields = "__all__"
        # field_classes = {"username": UsernameField}

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = ("employee_no","email")

class MyUserAdmin(UserAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("employee_no", "enmployee_name", "password")}),
        (_("Personal info"), {"fields": ("email",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("employee_no","employee_name","email", "password1", "password2"),
            },
        ),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ("employee_no","employee_name", "email", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("employee_no","employee_name", "email",)
    ordering = ("employee_no",)

admin.site.register(Employee, MyUserAdmin)
