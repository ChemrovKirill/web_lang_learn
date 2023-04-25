# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cards(models.Model):
    number = models.IntegerField()
    front_text = models.TextField()
    back_text = models.TextField()
    front_subtext = models.TextField()
    back_subtext = models.TextField()

    class Meta:
        managed = False
        db_table = 'cards'


class Vocabulary(models.Model):
    word = models.TextField()
    ru_translate = models.TextField()
    definition = models.TextField()
    example = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vocabulary'
