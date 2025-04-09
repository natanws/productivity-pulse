from django.db import models

class Task(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField(blank=True)
  is_completed = models.BooleanField(default=False)
  due_date = models.DateTimeField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.title
