from django.db import models
from django.contrib.auth import get_user_model
from api.config import PlanTiers, PostCategory


class Health(models.Model):
    """
    Simple Health model to track health check records.
    """
    status = models.CharField(
        max_length=20,
        choices=[
            ('healthy', 'Healthy'),
            ('degraded', 'Degraded'),
            ('unhealthy', 'Unhealthy'),
        ],
        default='healthy'
    )
    service_name = models.CharField(max_length=100, default='Django API')
    timestamp = models.DateTimeField(auto_now_add=True)
    response_time_ms = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = 'Health Records'
    
    def __str__(self):
        return f"{self.service_name} - {self.status} at {self.timestamp}"



class User(models.Model):
    username = models.CharField(max_length=100, default='Django API', primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    

class Post(models.Model):
    description = models.CharField(max_length=100, default='Django API')
    plans = models.CharField(
        max_length=50,
        choices=[(plan.value, plan.value) for plan in PlanTiers],
    )
    category = models.CharField(
        max_length=50,
        choices=[(cat.value, cat.value) for cat in PostCategory],
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'post',)

