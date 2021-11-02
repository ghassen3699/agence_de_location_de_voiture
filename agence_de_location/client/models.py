from django.db import models
from django.contrib.auth.models import User


class Client(models.Model) :
    nom = models.CharField(max_length=20, null=True)
    prenom = models.CharField(max_length=20, null=True)
    email = models.EmailField(unique=True, null=True)
    compte = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) :
        return self.email