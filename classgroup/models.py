from django.db import models


class Classgroup(models.Model):
    title = models.TextField()

    class Meta:
        db_table = "classgroup"
