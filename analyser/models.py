from django.contrib.auth.models import User
from django.db import models

class Analysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    analysis_result = models.TextField()