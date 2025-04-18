from django.db import models

class Tasks(models.Model):
    STATUS_CHOICES = [
        ('todo','ToDo'),
        ('inprogress', 'In Progress'),
        ('done', 'Done'),
    ]
    title = models.CharField(max_length=250)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES , default='todo')
    
    def __str__(self):
        return self.title