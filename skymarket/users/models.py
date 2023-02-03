from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField


class UserRoles:
    USER = "user"
    ADMIN = "admin"
    ROLE = [(USER, USER), (ADMIN, ADMIN)]


class User(AbstractBaseUser):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone = PhoneNumberField()
    role = models.CharField(max_length=5, choices=UserRoles.ROLE, default=UserRoles.USER)
    image = models.ImageField(upload_to="avatars/", null=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
