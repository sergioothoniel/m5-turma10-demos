from django.db import models


class Seasons(models.TextChoices):
    SUMMER = "Verão"
    AUTUMN = "Outono"
    WINTER = "Inverno"
    SPRING = "Primavera"
    DEFAULT = "Não especificado"


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    favorite_season = models.CharField(
        max_length=20, choices=Seasons.choices, default=Seasons.DEFAULT
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_full_name(self) -> str:
        # full_name = f"{self.first_name} {self.last_name}".title()

        # return full_name
        return f"{self.first_name} {self.last_name}".title()

    def __repr__(self) -> str:
        return f"<User {self.id} - {self.email}>"
