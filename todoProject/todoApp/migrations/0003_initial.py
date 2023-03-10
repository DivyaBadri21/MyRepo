# Generated by Django 4.1.3 on 2023-01-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('todoApp', '0002_delete_todoitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_complete', models.BooleanField(default=False)),
                ('task_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
