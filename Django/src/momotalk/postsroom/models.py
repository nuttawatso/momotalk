from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    title = models.CharField(max_length=50)

CATEGORY_CHOICES = (
    ('ทั่วไป', 'ทั่วไป'),
    ('ความรัก', 'ความรัก'),
    ('ปรึกษา', 'ปรึกษา'),
    ('การเรียน', 'การเรียน'),
)
    
    
    
    

class Posts(models.Model):
    def __str__(self):
        return f'{self.description},{self.title}'

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    datetime = models.DateTimeField(default=timezone.now)
    category= models.CharField(max_length=200 ,choices=CATEGORY_CHOICES, default='ทั่วไป')

    objects=models.Manager()