# Generated by Django 5.0.2 on 2024-03-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_project_design_project_data_project_descript_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolls',
            name='roll_name',
            field=models.CharField(max_length=50),
        ),
    ]
