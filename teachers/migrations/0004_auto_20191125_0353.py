# Generated by Django 2.2.7 on 2019-11-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_auto_20191108_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='expertise',
            field=models.ManyToManyField(blank=True, related_name='expert_in', to='teachers.Topic'),
        ),
    ]