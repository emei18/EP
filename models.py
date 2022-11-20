from django.db import models

class Entry(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Project(models.Model):
    preview = models.ImageField(blank=True, verbose_name='preview')
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(default=None)

    def __str__(self):
        return self.text
