from django import forms
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    user_type = (
        ("U", "User"),
        ("M", "Moderator"),
    )

    type = models.CharField(choices=user_type, max_length=1, default='U')

    picture = models.ImageField(upload_to='profile_pics', height_field=None, width_field=None, max_length=64, null=False, default='profile_pics/default.png')

    def __str__(self):
        return self.user.username

#Model manager for Proxy model (UserModerator)
class UserModeratorManager(models.Manager):
    def get_queryset(self):
        return super(UserModeratorManager, self).get_queryset().filter(type='M')

    def create(self, **kwargs):
        kwargs.update({'type': 'M'})

        return super(UserModeratorManager, self).create(**kwargs)

#Proxy Model
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
    #slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(Kitchen, self).save(*args, **kwargs)


# define Members-relation
class Members(models.Model):
    user_id = models.OneToOneField(
        User, on_delete=models.CASCADE)
    kitchen_id = models.OneToOneField(
        Kitchen, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user_id', 'kitchen_id'),)
        verbose_name_plural = 'Members'


# define Fridge-table
class Fridge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, null=False)
    full = models.BooleanField(default=False)


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
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


# define Oven-table
class Oven(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, null=False)
    free = models.BooleanField(default=True)


# define Stoves-table
class Stove(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    type = models.CharField(max_length=64, null=False)
    free = models.BooleanField(default=True)

