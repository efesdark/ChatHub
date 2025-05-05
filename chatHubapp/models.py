from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=10)  # "user" or "bot"
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

def __str__(self):
    text_preview = self.text[:30] if self.text else ""
    username = self.user.username if hasattr(self.user, 'username') else str(self.user)
    return f"{username} - {self.sender}: {text_preview}"
