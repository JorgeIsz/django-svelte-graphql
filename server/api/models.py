from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    name = models.CharField(_("Full name"), blank=True, max_length=255)
    first_name = None
    last_name = None

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Task(models.Model):
    name = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
