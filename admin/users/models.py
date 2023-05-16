from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import check_password

class MyUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return '{0},{1},{2},{3}'.format(self.first_name, self.last_name, self.email, self.password)

    def is_password_valid(self, password):
        return check_password(password, self.password)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['id']






