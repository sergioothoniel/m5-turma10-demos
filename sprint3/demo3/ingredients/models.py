from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=40)

    # N:N
    recipes = models.ManyToManyField("recipes.Recipe", related_name="ingredients")

    def __repr__(self) -> str:
        return f"<Ingredient {self.id} - {self.name}>"
