# Generated by Django 2.2.3 on 2019-07-15 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0011_auto_20190715_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobinfo',
            name='job_designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.Designation'),
        ),
        migrations.DeleteModel(
            name='Designation',
        ),
    ]