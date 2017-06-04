from django.db import models
from term.models import Term
# Create your models here.


class Jury(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('name', max_length=100)
    term = models.ForeignKey(Term, related_name="juries")
