# Generated by Django 3.1.4 on 2021-08-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]
