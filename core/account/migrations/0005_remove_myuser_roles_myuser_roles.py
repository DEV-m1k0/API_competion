# Generated by Django 4.2 on 2024-09-21 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_myuser_roles_myuser_roles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='roles',
        ),
        migrations.AddField(
            model_name='myuser',
            name='roles',
            field=models.ManyToManyField(blank=True, to='account.role'),
        ),
    ]