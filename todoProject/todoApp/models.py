from django.db import models

class TodoItem(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.TextField()
    task_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.task_name