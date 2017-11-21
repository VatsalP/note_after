from django.db import models


class Note(models.Model):
    note_id = models.CharField(max_length=8, primary_key=True)
    note = models.TextField()