# Generated by Django 4.2.7 on 2023-11-29 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_fitinsightbase_presence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fitinsightbase',
            name='presence',
        ),
        migrations.AlterField(
            model_name='fitinsightbase',
            name='attended',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]