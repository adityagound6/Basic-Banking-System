# Generated by Django 3.0.6 on 2021-03-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20210311_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transectionhistory',
            name='date_time',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
    ]
