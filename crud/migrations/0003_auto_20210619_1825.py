# Generated by Django 3.1.3 on 2021-06-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20210619_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tarefa',
            field=models.CharField(max_length=100, verbose_name='Task'),
        ),
    ]