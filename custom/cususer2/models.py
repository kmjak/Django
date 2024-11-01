from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
# from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.validators import UnicodeUsernameValidator

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, employee_no, password, **extra_fields):
        if not employee_no:
            raise ValueError("The given username must be set")

        employee = self.model(employee_no=employee_no, **extra_fields)
        employee.set_password(password)
        employee.save(using=self._db)
        return employee

    def create_user(self, employee_no, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(employee_no, password, **extra_fields)

    def create_superuser(self, employee_no, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(employee_no, password, **extra_fields)

class Employee(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    employee_no = models.CharField(_("従業員番号"), unique=True, max_length=6, blank=True)
    employee_name = models.CharField(_("従業員名"), max_length=30, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "employee_no"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("従業員")
        verbose_name_plural = _("従業員")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        return self.employee_no
