# Generated by Django 5.0.4 on 2024-04-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidcodercarnivalapi', '0003_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='type',
            field=models.CharField(choices=[('mcq', 'Multiple Choice Question'), ('code', 'Code Challenge')], max_length=100),
        ),
    ]
