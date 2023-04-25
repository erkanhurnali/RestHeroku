from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=250)
    body = models.CharField(max_length=250)
    description = models.CharField(null=True, max_length=250)
    def __str__(self) -> str:
        return self.title