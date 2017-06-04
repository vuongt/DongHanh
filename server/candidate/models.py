from django.db import models
from term.models import Term
from university.models import University
from jury.models import Jury


class Candidate(models.Model):
    TYPE_CHOICES = (
        ('CS', 'College Student'),
        ('HS', 'High School'),
    )
    SEX_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    id = models.BigAutoField(primary_key=True)

    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='CS')

    last_name = models.CharField('last_name', max_length=100, unique=False)
    first_name = models.CharField('first_name', max_length=100, unique=False)
    # True = Girl.
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=True)
    date_of_birth = models.DateField(null=True)
    field_of_study = models.TextField(blank=True)
    university = models.ForeignKey(University, related_name='candidates')
    college_year = models.IntegerField(null=True)
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    term = models.ForeignKey(Term, related_name="candidates")

    jury = models.ForeignKey(Jury, related_name="candidates")

    selected = models.BooleanField(default=False)