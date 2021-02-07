from django.db import models

# Create your models here.


class League(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, help_text="Replace spaces with '-'")

    def __str__(self):
        return self.name


class Season(models.Model):
    team = models.ManyToManyField(Team)
    year = models.CharField(max_length=10, help_text="Format (YYYY-YYYY)")

    def __str__(self):
        return self.year
