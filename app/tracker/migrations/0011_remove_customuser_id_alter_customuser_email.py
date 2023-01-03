# Generated by Django 4.1.4 on 2023-01-03 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True),
        ),
    ]
