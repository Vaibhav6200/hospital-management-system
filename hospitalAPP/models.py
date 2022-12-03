from django.db import models
from django.urls import reverse


class Departments(models.Model):
    name = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(max_length=25, unique=True)
    icon = models.ImageField(upload_to="Departments")
    discrpition = models.TextField(max_length=200)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
    def get_urls(self):
        return reverse('depview', args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)
class Doctors(models.Model):
    doc_name = models.CharField(max_length=25, unique=True)
    departments = models.ForeignKey(Departments, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to="Doctors")
    numbers = models.CharField(max_length=12) 
    available = models.BooleanField(default=True)       
    class Meta:
        ordering = ('departments',)
        verbose_name = 'Docter'
        verbose_name_plural = 'Doctories'
    def get_urls(self):
        return reverse('depview', args=[self.departments.slug, self.slug])


    def __str__(self):
        return '{}'.format(self.doc_name)
