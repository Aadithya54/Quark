# Generated by Django 5.0.2 on 2024-03-04 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_data_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='institution',
            field=models.CharField(max_length=200),
        ),
    ]
