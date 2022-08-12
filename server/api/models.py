from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    name = CharField(_("Full name"), blank=True, max_length=255)
    first_name = None
    last_name = None

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
