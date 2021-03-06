# Generated by Django 3.1.2 on 2020-10-11 15:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('willdo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='willdomodel',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='willdomodel',
            name='priority',
            field=models.CharField(choices=[('danger', '高'), ('warning', '中'), ('info', '低')], default='danger', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='willdomodel',
            name='task_type',
            field=models.CharField(choices=[('item1', 'ファーストタスク'), ('item2', 'メール'), ('item3', '書類'), ('item4', 'すぐ終わる'), ('item5', 'デイリータスク')], default='item1', max_length=40),
            preserve_default=False,
        ),
    ]
