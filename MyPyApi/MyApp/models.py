# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Movies(models.Model):
    index = models.AutoField(primary_key=True)#(blank=True, null=True)
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=False, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    movie = models.TextField(blank=False, null=False)
    year = models.BigIntegerField(blank=False, null=False)
    timemin = models.BigIntegerField(db_column='timeMin', blank=False, null=False)  # Field name made lowercase.
    imdb = models.FloatField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'Movies'
