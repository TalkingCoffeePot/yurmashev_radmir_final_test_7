from django.db import models

# Create your models here.

status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]

class GuestCard(models.Model):
    name = models.CharField('Имя автора', max_length=100, null=False, blank=False)
    mail = models.EmailField('Эл. почта', max_length=200, null=False, blank=False)
    date_create = models.DateTimeField('Время создания', auto_now_add=True)
    date_edit = models.DateTimeField('Время редактирования', auto_now=True)
    description = models.TextField('Детали задачи', max_length=1500, null=False, blank=True)
    card_status = models.CharField('Текущий статус', max_length=50, null=False, blank=False, choices=status_choices, default=status_choices[0])
        
    def __str__(self):
        return f'{self.pk}, {self.name}, {self.card_status}, {self.date_create}, {self.date_edit}' 