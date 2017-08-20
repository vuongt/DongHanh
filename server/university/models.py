from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from django.core.urlresolvers import reverse
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL')
# Create your models here.


class University(models.Model):
    """
    Represent an university
    """
    id = models.BigAutoField(primary_key=True)

    name = models.CharField('University Name', max_length=50, unique=True)
    code = models.CharField('University code', max_length=10, unique=True)
    about = models.TextField(blank=True)

    created_on = models.DateTimeField('created_on', auto_now_add=True)
    created_by = models.ForeignKey(AUTH_USER_MODEL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Universities"

    def get_absolute_url(self):
        return reverse('university:list', args=())
