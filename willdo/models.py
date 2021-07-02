from django.db import models
import datetime

# Create your models here.
TASK_TYPE = (
    ('item1','ファーストタスク'),
    ('item2','メール'),
    ('item3','書類'),
    ('item4','すぐ終わる'),
    ('item5','デイリータスク')
    )
PRIORITY = (
    ('danger','高'),
    ('warning','中'),
    ('info','低')
    )

class WilldoModel(models.Model):
    title = models.CharField(max_length=40)
    note = models.TextField()
    task_type = models.CharField(
        max_length = 40,
        choices = TASK_TYPE
    )
    priority = models.CharField(
        max_length = 40,
        choices = PRIORITY
    )
    date = models.DateField(default=datetime.date.today)
    create_user = models.CharField(max_length=20)
    def __str__(self):
        return self.title
