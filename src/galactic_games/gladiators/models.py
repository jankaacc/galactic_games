from django.db import models


class Profession(models.Model):
    name = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Species(models.Model):
    name = models.CharField(max_length=120)
    planet = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=120)
    skin_color = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Gladiator(models.Model):
    name = models.CharField(max_length=120)
    profession = models.ForeignKey(Profession)
    species = models.ForeignKey(Species)
    race = models.ForeignKey(Race)
    hp = models.IntegerField(default=100)

    def __str__(self):
        return "Name: {}, Profession: {}, Species: {}, Race: {}".format(
            self.name, self.profession, self.species, self.race)
