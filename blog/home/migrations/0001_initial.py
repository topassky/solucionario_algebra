# Generated by Django 4.1.3 on 2022-11-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='solucionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ejercicio', models.CharField(max_length=200, verbose_name='id_ejercicio')),
            ],
            options={
                'verbose_name': 'solucionario',
                'db_table': 'solucionario',
                'ordering': ['id'],
            },
        ),
    ]