# Generated by Django 4.1.6 on 2023-02-13 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_alter_todo_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="status",
            field=models.IntegerField(
                choices=[(1, "In progress"), (0, "Finished")], default=1
            ),
        ),
    ]
