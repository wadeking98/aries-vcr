from django.db import models
from django.contrib.postgres import fields as contrib
from .Auditable import Auditable


class Schema(Auditable):
    name = models.TextField()
    version = models.TextField()
    origin_did = models.TextField()
    schema_label = contrib.JSONField(blank=True, null=True)

    class Meta:
        db_table = "schema"
        unique_together = (("name", "version", "origin_did"),)
        ordering = ("id",)
