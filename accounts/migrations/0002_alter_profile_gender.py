# Generated by Django 4.2 on 2023-04-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male')], default='not found', max_length=100),
        ),
    ]
