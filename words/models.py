from django.db import models
from accounts.models import User


class Section(models.Model):
    name = models.CharField(verbose_name="Section Name", max_length=200)
    user = models.ForeignKey(User, related_name='sections', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Sections"

    def __str__(self):
        return self.name


class Word(models.Model):
    foreign_word = models.CharField(verbose_name="Foreign Word", max_length=200)
    native_word = models.CharField(verbose_name="Native Word", max_length=200)
    section = models.ForeignKey(Section, related_name='words', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"

    def __str__(self):
        return f"{self.foreign_word} - {self.native_word}"
