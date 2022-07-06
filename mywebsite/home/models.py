from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=220)
    phone = models.IntegerField()
    textarea = models.CharField(max_length=300)


class Suggest(models.Model):
    sname = models.CharField(max_length=220)
    smessage = models.TextField(max_length=500)
