# Generated by Django 4.1.4 on 2023-01-02 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user_is_doctor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Prescription',
        ),
    ]
