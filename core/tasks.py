from celery import shared_task
from .models import Workflow, Task

@shared_task
def execute_task(task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = True
    task.save()

@shared_task
def execute_workflow(workflow_id):
    workflow = Workflow.objects.get(id=workflow_id)
    for task in workflow.tasks.order_by('order'):
        execute_task.delay(task.id)