# Generated by Django 2.0.5 on 2018-06-18 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
