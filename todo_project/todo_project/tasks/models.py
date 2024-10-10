from django.db import models
from datetime import date

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True, null = True)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)

    @property
    def completed(self):
        if self.due_date > date.today():
            return "Incoming"
        
        elif self.due_date == date.today():
            return "Today"
        
        elif self.due_date < date.today():
            return "Overdue"
    
    def __str__(self):
        return self.title
