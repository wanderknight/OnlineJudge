from django.db import models
from account.models import User


class Classgroup(models.Model):
    title = models.TextField()
    users = models.ManyToManyField(User)

    class Meta:
        db_table = "classgroup"
