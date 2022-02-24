from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.title}: {self.desc}'
