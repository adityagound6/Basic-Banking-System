# Generated by Django 3.0.6 on 2021-03-10 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_transectionhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transectionhistory',
            name='from_account',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transectionhistory',
            name='to_account',
            field=models.IntegerField(),
        ),
    ]