from django.db import models
from django.utils import timezone
import datetime

class Auther(models.Model):
    name = models.CharField(max_length = 30)
    designation = models.CharField(max_length = 20)
    topic = models.CharField(max_length = 20)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
class Content(models.Model):
    content = models.ForeignKey(Auther, on_delete = models.CASCADE)
    content_text = models.TextField()
    def __str__(self):
        return self.content_text