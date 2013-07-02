from django.db import models

class Bag(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)

    def __repr__(self):
        return "%s: %s" % (self.__class__, self.name)

    def __str__(self):
        return "%s: %s" % (self.__class__, self.name)

class Vegetable(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    bag = models.ForeignKey(Bag, related_name="vegetables")

    def __repr__(self):
        return "%s: %s" % (self.__class__, self.name)

    def __str__(self):
        return "%s: %s" % (self.__class__, self.name)
