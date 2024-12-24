from rest_framework import serializers
from .models import Workflow, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model =Task
        fields = '__all__'

class WorkflowSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False)

    class Meta:
        model= Workflow
        fields = '__all__'

    def create(self, validated_data):
        tasks_data =validated_data.pop('tasks', [])
        workflow = Workflow.objects.create(**validated_data)
        for task_data in tasks_data:
            Task.objects.create(workflow=workflow, **task_data)
        return workflow
    
    def update(self, instance, validated_data):
        tasks_data = validated_data.pop('tasks', [])
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        for task_data in tasks_data:
            task_id = task_data.get('id', None)
            if task_id:
                task = Task.objects.get(id=task_id, workflow=instance)
                task.name = task_data.get('name', task.name)
                task.order = task_data.get('order', task.order)
                task.scheduled_time = task_data.get('scheduled_time', task.scheduled_time)
                task.save()
            else:
                Task.objects.create(workflow=instance, **task_data)

        return instance