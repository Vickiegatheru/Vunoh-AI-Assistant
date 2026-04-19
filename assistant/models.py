from django.db import models
import uuid

class Task(models.Model):
    # Unique code for tracking [cite: 53]
    task_code = models.CharField(max_length=12, unique=True, editable=False)
    intent = models.CharField(max_length=50) # [cite: 34]
    entities = models.JSONField(default=dict) # [cite: 35]
    risk_score = models.IntegerField() # [cite: 49]
    status = models.CharField(max_length=20, default='Pending') # [cite: 55]
    steps = models.JSONField(default=list) # [cite: 57]
    
    # Message formats [cite: 61-65]
    whatsapp_msg = models.TextField()
    email_msg = models.TextField()
    sms_msg = models.TextField()
    
    assigned_to = models.CharField(max_length=100) # [cite: 71]
    created_at = models.DateTimeField(auto_now_add=True) # [cite: 56]

    def save(self, *args, **kwargs):
        if not self.task_code:
            self.task_code = f"VNH-{uuid.uuid4().hex[:6].upper()}"
        super().save(*args, **kwargs)