from django.db import models
from users.models import User
from django.utils import timezone
# Create your models here.


class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.id:
            save_instance = TodoList.objects.get(id=self.id)
            if save_instance.is_complete != self.is_complete:
                if self.is_complete:
                    self.completion_at = timezone.now()
                else:
                    self.completion_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)
