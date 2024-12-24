from django.db import models

# Create your models here.
class Workflow(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    workflow = models.ForeignKey(Workflow, related_name='tasks', on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    order = models.PositiveBigIntegerField()
    is_completed = models.BooleanField(default=False)
    scheduled_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} in {self.workflow.name}"
