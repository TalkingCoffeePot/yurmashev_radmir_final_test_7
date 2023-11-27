from django.db import models

# Create your models here.

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Task(models.Model):
    description = models.TextField(max_length=500, null=False, blank=False, verbose_name='Описание')
    task_status = models.CharField(max_length=50, null=False, blank=False, verbose_name='Текущий статус', choices=status_choices, default=status_choices[0])
    date = models.CharField(max_length=10, null=False, blank=True, verbose_name='Сделать до...', default='yyyy-mm-dd')

    def __str__(self):
        return f'{self.pk}, {self.description}, {self.task_status}, {self.date}' 