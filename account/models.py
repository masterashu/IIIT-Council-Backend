from django.db import models
from base.models import College, Subject
from registration.models import User
# Create your models here.


class Profile(models.Model):
    pass


class Permission(models.Model):
    name = models.CharField(max_length=80)


class Role(models.Model):
    user = models.ForeignKey(to=User, related_name='roles', on_delete=models.Model)
    # name = models.CharField(max_length=)
    permission = models.ManyToManyField(to=Permission)


class CustomRole(Role):
    name = models.CharField(max_length=80)
    college = models.ForeignKey(to=College, on_delete=models.Model)


class Moderator(Role):
    name = models.CharField(max_length=80)
    college = models.ManyToManyField(to=College, related_name='moderators')


class Director(Role):
    college = models.OneToOneField(to=College, related_name='director', on_delete=models.CASCADE)

    @property
    def name(self):
        return 'Director'


class PastDirector(Role):
    college = models.ForeignKey(to=College, related_name='past_directors', on_delete=models.CASCADE)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    @property
    def name(self):
        return 'PastDirector'


class Admin(Role):
    college = models.OneToOneField(to=College, related_name='admin', on_delete=models.CASCADE)

    @property
    def name(self):
        return 'Admin'


class Professor(Role):
    college = models.ForeignKey(to=College, related_name='professors', on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    subjects = models.ManyToManyField(to=Subject)

