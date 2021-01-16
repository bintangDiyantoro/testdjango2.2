from django.db import models
from django.utils.text import slugify
from .validators import validatePenulis
from django.urls import reverse
# Create your models here.


class Artikel(models.Model):
    judul = models.CharField(max_length=20, unique=True)
    isi = models.TextField(
        max_length=300, default="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Et repudiandae reiciendis quos rem, consequatur debitis eveniet ullam perspiciatis cum eum?")
    penulis = models.CharField(max_length=30, validators=[validatePenulis])
    slug = models.SlugField(blank=True, editable=False)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self):
        self.slug = slugify(self.judul)
        return super(Artikel, self).save()

    def get_absolute_url(self):
        return reverse('blog:index')

    def __str__(self):
        return self.judul
