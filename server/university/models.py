from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL')
# Create your models here.


class University(models.Model):
    """
    Represent an university
    """
    id = models.BigAutoField(primary_key=True)

    name = models.CharField('University Name', max_length=50, unique=True)
    code = models.CharField('University short name', max_length=10, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    about = models.TextField(blank=True)

    created_on = models.DateTimeField('created_on', auto_now_add=True)
    created_by = models.ForeignKey(AUTH_USER_MODEL)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(University, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Universities"
