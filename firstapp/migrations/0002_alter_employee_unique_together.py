# Generated by Django 4.2.3 on 2023-07-04 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together={('name', 'phone', 'date_of_birth')},
        ),
    ]
