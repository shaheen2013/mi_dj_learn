from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Todos'
