# Generated by Django 3.0.2 on 2020-01-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0021_auto_20200116_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]