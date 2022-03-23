from django.db import models
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=254)
    content = models.TextField(validators=[
        MinLengthValidator(10, 'Value must be greater than 10!')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
