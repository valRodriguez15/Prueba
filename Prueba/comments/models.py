from django.db import models
from users.models import User
from categories.models import Tours

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE, null=True)

