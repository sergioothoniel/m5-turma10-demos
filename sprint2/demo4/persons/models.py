from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True, blank=True)
    married = models.BooleanField(null=True, blank=True, default=False)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2)

    # auto_now_add -> criado 1x só
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now -> atualizar a data sempre que o registro sofrer alterações no banco
    updated_at = models.DateTimeField(auto_now=True)
