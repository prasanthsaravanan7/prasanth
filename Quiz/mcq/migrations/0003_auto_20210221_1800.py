# Generated by Django 3.1.3 on 2021-02-21 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0002_auto_20210221_1725'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='quiz_category',
        ),
        migrations.AlterModelTable(
            name='questions',
            table='quiz_questions',
        ),
    ]
