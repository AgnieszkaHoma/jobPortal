# Generated by Django 4.0.1 on 2022-06-03 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0007_alter_application_introduceyourself_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='application',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='application',
            name='introduceYourself',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='backend.job'),
        ),
    ]
