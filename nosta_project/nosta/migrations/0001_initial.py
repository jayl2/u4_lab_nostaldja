# Generated by Django 4.1 on 2022-08-30 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_year', models.CharField(max_length=4)),
                ('end_year', models.CharField(max_length=4)),
            ],
        ),
    ]
