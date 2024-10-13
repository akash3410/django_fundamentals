from django.db import models

# Create your models here.
class Items(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    updated_by = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title
    
