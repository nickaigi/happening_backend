from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class News(models.Model):
    """
    Model to hold a News Items
    """
    user = models.ForeignKey(User, verbose_name='Reported by')
    title = models.CharField(max_length=200)
    story = models.TextField(max_length=500)
    timestamp = models.DateTimeField(blank=True, verbose_name='Date Published', null=True)
    last_edited = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'News Items'
        verbose_name = 'News'
        ordering = ['-timestamp']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)


class Tag(models.Model):
    """
    Model for Tags associated with Stories
    """
    user = models.ForeignKey(User, verbose_name='Created by')
    news = models.ForeignKey(News, verbose_name='Tagged News')
    title = models.CharField(max_length=50)
    timestamp = models.DateTimeField(blank=True, verbose_name='Date Created')
    last_edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tag'

    def __unicode__(self):
        return self.title
