# Generated by Django 2.1.7 on 2019-03-13 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user1',
            name='birth_date',
            field=models.DateField(default='Date of birth: '),
        ),
    ]
