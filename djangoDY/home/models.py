from django.db import models
from unittest.util import _MAX_LENGTH

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    createDate = models.DateTimeField()
    
