# from django.db import models
# from django.template.defaultfilters import slugify
# from django.conf import settings
# AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL')
#
# # Create your models here.
#
#
# class Term(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=50, unique=True)
#     year = models.CharField(max_length=4, null=True)
#     prez_fr = models.CharField(max_length=100, null=True)
#     prez_tw = models.CharField(max_length=100, null=True)
#     prez_sg = models.CharField(max_length=100, null=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Term, self).save(*args, **kwargs)
#
# class University(models.Model):
#     """
#     Represent an university
#     """
#     id = models.BigAutoField(primary_key=True)
#
#     name = models.CharField('University Name', max_length=50, unique=True)
#     short_name = models.CharField('University short name', max_length=10, unique=True)
#     slug = models.SlugField(max_length=60, unique=True)
#     about = models.TextField(blank=True)
#
#     created_on = models.DateTimeField('created_on', auto_now_add=True)
#     created_by = models.ForeignKey(AUTH_USER_MODEL)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(University, self).save(*args, **kwargs)
#
# class Jury(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField('name', max_length=100)
#     term = models.ForeignKey(Term, related_name="juries")
#
#
# class Candidate(models.Model):
#     TYPE_CHOICES = (
#         ('CS', 'College Student'),
#         ('HS', 'High School'),
#     )
#     id = models.BigAutoField(primary_key=True)
#
#     type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='CS')
#
#     last_name = models.CharField('last_name', max_length=100, unique=False)
#     first_name = models.CharField('first_name', max_length=100, unique=False)
#     # True = Girl.
#     sex = models.BooleanField(null=True)
#     date_of_birth = models.DateField(null=True)
#     field_of_study = models.TextField(blank=True)
#     university = models.ForeignKey(University, related_name='candidates')
#     college_year = models.IntegerField(null=True)
#     address = models.TextField(blank=True)
#     email = models.EmailField(unique=True)
#
#     term = models.ForeignKey(Term, related_name="candidates")
#
#     jury = models.ForeignKey(Jury, related_name="candidates")
#
#     selected = models.BooleanField(default=False)
#
#
#
#
#
# class Evaluation(models.Model):
#     LOCATION_CHOICES = (
#         ('FR', 'France'),
#         ('TW', 'Taiwan'),
#         ('SG', 'Singapore'),
#     )
#     id = models.BigAutoField(primary_key=True)
#     university = models.ForeignKey(University, related_name='coefficients')
#     evaluated_by = models.CharField(max_length=2, choices=LOCATION_CHOICES, default='FR')
#     vn_coef = models.IntegerField(default=0)
#     jury_by_copy = models.IntegerField(default=3)
#     max_by_jury = models.IntegerField(default=12)
#
#
#
