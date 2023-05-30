from django.db import models
from utils.generator import code_generator
from users.models import CustomUser

# Create your models here.

class Workspace(models.Model):

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=150, null=False)
    code = models.CharField(default=code_generator, max_length=19)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255, null=True)


class Membership(models.Model):

    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
