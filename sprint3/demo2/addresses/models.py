from django.db import models

# from users.models import User


# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=50)
    number = models.IntegerField()
    complement = models.CharField(max_length=50, null=True, blank=True)

    # FK 1:1
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    # models.PROTECT
    # models.RESTRICT
