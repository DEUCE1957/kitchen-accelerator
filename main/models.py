from django import forms
from django.db import models
import re
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import uuid
import random
import string


used_strings = []
def random_string(string_length=10):
    letters = string.ascii_lowercase
    new_random = ''.join(random.choice(letters) for i in range(string_length))
    if new_random not in used_strings:
        return new_random
    else:
        random_string()
    
# define userprofile table
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # define user classes
    user_type = (
        ("U", "User"),
        ("M", "Moderator"),
    )
    # set user class
    type = models.CharField(choices=user_type, max_length=1, default='U')
    # profilepicture
    picture = models.ImageField(upload_to='profile_pics', height_field=None, 
        width_field=None, max_length=64, null=False, default='profile_pics/default.png')

    def __str__(self):
        return self.user.username


# Model manager for Proxy model (UserModerator)
class UserModeratorManager(models.Manager):
    def get_queryset(self):
        return super(UserModeratorManager, self).get_queryset().filter(type='M')

    def create(self, **kwargs):
        kwargs.update({'type': 'M'})

        return super(UserModeratorManager, self).create(**kwargs)


# Proxy Model
class UserModerator(UserProfile):
    objects = UserModeratorManager()

    class Meta:
        proxy = True


# define Kitchen-table
class Kitchen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.CharField(max_length=64, null=False)
    name = models.CharField(max_length=64, null=False)
    fridges = models.IntegerField(default=0)
    ovens = models.IntegerField(default=0)
    stoves = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name) #sets slug
        super(Kitchen, self).save(*args, **kwargs)


# define Members-relation
class Members(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)
    kitchen = models.ForeignKey(
        Kitchen, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields= ['user','kitchen'], name='unique users')]
        verbose_name_plural = 'Members'


# define Fridge-table
class Fridge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, null=False)
    full = models.BooleanField(default=False)
    name = models.CharField(default=random_string, max_length=32)


# define Shelf-table
class Shelf(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE, null=False)
    full = models.BooleanField(default=False)


# define Cell-table
class Cell(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, null=False)
    full = models.BooleanField(default=False)
    owner = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)


# define Oven-table
class Oven(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, null=False)
    free = models.BooleanField(default=True)
    name = models.CharField(default=random_string, max_length=32)
    owner = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)


# define Stoves-table
class Stove(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    type = models.CharField(max_length=64, null=False)
    free = models.BooleanField(default=True)
    name = models.CharField(default=random_string, max_length=32)
    owner = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    

def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):
    """
    Calculates and stores a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug, limiting its length if necessary.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create the queryset if one wasn't explicitly provided and exclude the
    # current instance from the queryset.
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len-len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    # Remove multiple instances and if an alternate separator is provided,
    # replace the default '-' separator.
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    # Remove separator from the beginning and end of the slug.
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value