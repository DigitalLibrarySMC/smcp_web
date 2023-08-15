from django.db import models
from quizes.models import Quiz
from django.conf import settings
# Create your models here.

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='results')
    score = models.FloatField()
    time = models.FloatField()

    def __str__(self):
        return str(self.pk)