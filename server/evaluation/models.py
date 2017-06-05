from django.db import models
from university.models import University
from jury.models import Jury
from candidate.models import Candidate
from term.models import Term
# Create your models here.


class EvaluationParameter(models.Model):
    LOCATION_CHOICES = (
        ('FR', 'France'),
        ('TW', 'Taiwan'),
        ('SG', 'Singapore'),
    )
    id = models.BigAutoField(primary_key=True)
    university = models.ForeignKey(University, related_name='parameters')
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES, default='FR')
    vn_coef = models.IntegerField(default=0)
    jury_by_copy = models.IntegerField(default=3)
    max_by_jury = models.IntegerField(default=12)


class Evaluation(models.Model):
    id = models.BigAutoField(primary_key=True)
    term = models.ForeignKey(Term, related_name='evaluations', null = True)
    jury = models.ForeignKey(Jury, related_name='evaluations', null = True)
    candidate = models.OneToOneField(Candidate, related_name='evaluation', null=True)
    background = models.FloatField(verbose_name='Family background', default=0)
    academic = models.FloatField(verbose_name='Academic records', default=0)
    motivation = models.FloatField(verbose_name='Dream and motivation', default=0)
    bonus = models.FloatField(verbose_name='Bonus', default=0)
