# Generated by Django 4.0.1 on 2022-06-04 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_alter_job_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-published']},
        ),
        migrations.RemoveField(
            model_name='job',
            name='image',
        ),
    ]
