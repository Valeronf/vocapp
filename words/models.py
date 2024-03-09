from django.db import models
import datetime
# Create your models here.
# yourappname/models.py

    

class Theme(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name

class Word(models.Model):
    original_word = models.CharField(max_length=100)
    translated_word = models.CharField(max_length=100)
    transcription = models.CharField(max_length=100, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.original_word} - {self.translated_word}"