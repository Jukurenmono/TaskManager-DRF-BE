# Generated by Django 5.1.2 on 2024-10-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_task_priority_task_updated_at_alter_task_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
