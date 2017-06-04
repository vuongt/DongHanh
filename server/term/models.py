from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Term(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    year = models.CharField(max_length=4, null=True)
    prez_fr = models.CharField(max_length=100, null=True)
    prez_tw = models.CharField(max_length=100, null=True)
    prez_sg = models.CharField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Term, self).save(*args, **kwargs)