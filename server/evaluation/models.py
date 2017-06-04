from django.db import models
from university.models import University

# Create your models here.

class Evaluation(models.Model):
    LOCATION_CHOICES = (
        ('FR', 'France'),
        ('TW', 'Taiwan'),
        ('SG', 'Singapore'),
    )
    id = models.BigAutoField(primary_key=True)
    university = models.ForeignKey(University, related_name='coefficients')
    evaluated_by = models.CharField(max_length=2, choices=LOCATION_CHOICES, default='FR')
    vn_coef = models.IntegerField(default=0)
    jury_by_copy = models.IntegerField(default=3)
    max_by_jury = models.IntegerField(default=12)