# Generated by Django 3.2.7 on 2021-10-10 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20211011_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='RollNo',
            field=models.TextField(default=1, null=True),
        ),
    ]