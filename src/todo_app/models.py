from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


TIMEFRAME_CHOICES = (
    ('td', 'Today'),
    ('wk', 'This Week'),
    ('mnth', 'This Month'),
    ('sp', 'In My Spare Time'),
)

class Task_model(models.Model):
    timeframe   = models.CharField(max_length=20, choices=TIMEFRAME_CHOICES, default='Today')
    title       = models.CharField(max_length=200)
    date        = models.DateField(default = date.today, blank=True)
    description = models.TextField()
    completed   = models.BooleanField(default=False)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
                          
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('task_home')

