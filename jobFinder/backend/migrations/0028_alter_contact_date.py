# Generated by Django 4.0.1 on 2022-06-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0027_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
