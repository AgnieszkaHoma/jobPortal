# Generated by Django 4.0.1 on 2022-06-02 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_application_created_by_application_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
